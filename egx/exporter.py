from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

N3_FIELDS = ("ID", "TYPE", "V", "TH", "RISK", "PROD", "CONF", "N2", "N1", "NEXT", "WHY")
VERDICTS = {"KEEP", "ADAPT", "REJECT", "WATCH"}
FORMATS = {"md", "json", "yaml", "mcp"}
PAYLOAD_KEYS = (
    "schema_version",
    "title",
    "source",
    "source_slug",
    "ingestion_date",
    "verdict",
    "confidence",
    "tags",
    "next_action",
    "model_used",
    "tokens",
    "density_score",
    "duplicate",
    "duplicate_refs",
    "n3",
    "paths",
)


def _today() -> str:
    return datetime.now().astimezone().date().isoformat()


def parse_n3(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if "=" not in line or line.startswith("#"):
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key in N3_FIELDS:
            data[key] = value.strip()
    return data


def render_n3(data: dict[str, str]) -> str:
    return "\n".join(f"{key}={data.get(key, 'none')}" for key in N3_FIELDS) + "\n"


def update_index_ref(root: Path, slug: str) -> None:
    index = root / "memory" / "INDEX.n3"
    ref = f"REF=memory/{slug}.n3"
    text = index.read_text(encoding="utf-8") if index.exists() else ""
    if ref not in text:
        index.write_text(text.rstrip() + "\n" + ref + "\n", encoding="utf-8")


def _slug(source: str) -> str:
    from .ingest import source_id

    return source_id(source)


def _card_path(root: Path, source: str) -> Path:
    direct = root / "memory" / source
    if direct.exists():
        return direct
    slug = source if source.endswith(".n3") else _slug(source)
    return root / "memory" / f"{Path(slug).stem}.n3"


def _source_from_n1(root: Path, data: dict[str, str], fallback: str) -> str:
    n1 = data.get("N1", "none")
    path = root / n1 if n1 != "none" else None
    if not path or not path.exists():
        return fallback
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("Source:"):
            return line.split(":", 1)[1].strip() or fallback
    return fallback


def _tags(data: dict[str, str]) -> list[str]:
    tags = ["n3", data.get("TYPE", "source")]
    theme = data.get("TH", "none")
    verdict = data.get("V", "WATCH").lower()
    if theme != "none":
        tags.append(theme)
    tags.append(verdict)
    return list(dict.fromkeys(tags))


def _duplicate_refs(root: Path, slug: str, source: str, current: Path) -> list[str]:
    refs: list[str] = []
    index = root / "memory" / "INDEX.n3"
    if index.exists() and index.read_text(encoding="utf-8").count(f"REF=memory/{slug}.n3") > 1:
        refs.append("memory/INDEX.n3")
    for path in sorted((root / "memory").glob("*.n3")):
        if path == current or path.name == "INDEX.n3":
            continue
        text = path.read_text(encoding="utf-8")
        if slug in path.stem or source in text:
            refs.append(path.relative_to(root).as_posix())
    return refs


def _density(data: dict[str, str]) -> int:
    score = 0
    score += 10 if data.get("V") in VERDICTS else 0
    score += 5 if data.get("TH", "none") != "none" else 0
    score += 10 if data.get("N2", "none") != "none" else 0
    score += 10 if data.get("N1", "none") != "none" else 0
    score += 10 if len(data.get("NEXT", "")) >= 6 else 0
    score += 10 if len(data.get("WHY", "")) >= 8 else 0
    score += {"LOW": 0, "MED": 10, "HIGH": 20}.get(data.get("CONF"), 0)
    score += {"WATCH": 5, "REJECT": 5, "ADAPT": 12, "KEEP": 15}.get(data.get("V"), 0)
    score += {"HIGH": 0, "MED": 5, "LOW": 10}.get(data.get("RISK"), 0)
    return min(score, 100)


def _payload(root: Path, source: str, config: dict[str, Any]) -> dict[str, Any]:
    path = _card_path(root, source)
    text = path.read_text(encoding="utf-8")
    data = parse_n3(text)
    if data.get("V") not in VERDICTS:
        data["V"] = "WATCH"
    slug = data.get("ID") or path.stem
    duplicates = _duplicate_refs(root, slug, source, path)
    payload = {
        "schema_version": "egx.n3.export.v1",
        "title": slug,
        "source": _source_from_n1(root, data, source),
        "source_slug": slug,
        "ingestion_date": _today(),
        "verdict": data["V"],
        "confidence": data.get("CONF", "LOW"),
        "tags": _tags(data),
        "next_action": "merge-duplicate" if duplicates else data.get("NEXT", "inspect-source"),
        "model_used": config.get("model", "default"),
        "tokens": int(config.get("tokens", 0) or 0),
        "density_score": _density(data),
        "duplicate": bool(duplicates),
        "duplicate_refs": duplicates,
        "n3": {key: data.get(key, "none") for key in N3_FIELDS},
        "paths": {
            "n3": path.relative_to(root).as_posix(),
            "n2": data.get("N2", "none"),
            "n1": data.get("N1", "none"),
        },
    }
    _validate_payload(payload)
    return payload


def _validate_payload(payload: dict[str, Any]) -> None:
    keys = set(payload)
    expected = set(PAYLOAD_KEYS)
    if keys != expected:
        raise ValueError(f"Invalid export schema keys: {sorted(keys ^ expected)}")
    if payload["verdict"] not in VERDICTS:
        raise ValueError(f"Invalid verdict: {payload['verdict']}")
    if not isinstance(payload["tags"], list) or not isinstance(payload["duplicate_refs"], list):
        raise ValueError("Invalid export schema list field")
    if not 0 <= int(payload["density_score"]) <= 100:
        raise ValueError("Invalid density_score")
    if set(payload["n3"]) != set(N3_FIELDS):
        raise ValueError("Invalid N3 field set")


def _display_path(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def _frontmatter(payload: dict[str, Any]) -> str:
    keys = (
        "title",
        "source",
        "ingestion_date",
        "verdict",
        "confidence",
        "tags",
        "next_action",
        "model_used",
        "tokens",
        "density_score",
    )
    return yaml.safe_dump({key: payload[key] for key in keys}, sort_keys=False).strip()


def render_payload(payload: dict[str, Any], fmt: str) -> str:
    if fmt not in FORMATS:
        raise ValueError(f"Unsupported export format: {fmt}")
    if fmt == "json":
        return json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if fmt == "yaml":
        return yaml.safe_dump(payload, sort_keys=False)
    if fmt == "mcp":
        mcp = {
            "schema_version": "egx.mcp.resource.v1",
            "resources": [
                {
                    "uri": f"egx://memory/{payload['source_slug']}",
                    "name": payload["title"],
                    "mimeType": "text/plain",
                    "text": render_n3(payload["n3"]),
                    "metadata": {key: payload[key] for key in payload if key not in {"n3"}},
                }
            ],
        }
        return json.dumps(mcp, indent=2, sort_keys=True) + "\n"
    return f"---\n{_frontmatter(payload)}\n---\n{render_n3(payload['n3'])}"


def export_card(root: Path, source: str, config: dict[str, Any], fmt: str = "md", output: Path | None = None) -> str:
    fmt = fmt.lower()
    if fmt not in FORMATS:
        raise ValueError(f"Unsupported export format: {fmt}")
    payload = _payload(root, source, config)
    suffix = "md" if fmt == "md" else fmt
    out = output or root / "memory" / "exports" / f"{payload['source_slug']}-N3.{suffix}"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_payload(payload, fmt), encoding="utf-8")
    return _display_path(root, out)


def _hash_vector(text: str, size: int = 16) -> list[float]:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return [round((digest[i] / 255.0), 6) for i in range(size)]


def export_vector(root: Path, source: str, config: dict[str, Any]) -> str:
    try:
        import lancedb  # type: ignore
    except ImportError as exc:
        raise RuntimeError("LanceDB missing. Install: pip install -e .[vector]") from exc

    payload = _payload(root, source, config)
    text = render_n3(payload["n3"])
    row = {
        "id": payload["source_slug"],
        "vector": _hash_vector(text),
        "text": text,
        "metadata": json.dumps({k: v for k, v in payload.items() if k != "n3"}, sort_keys=True),
    }
    db_path = root / "memory" / "exports" / "lancedb"
    db_path.mkdir(parents=True, exist_ok=True)
    db = lancedb.connect(str(db_path))
    if "n3_cards" in db.table_names():
        db.open_table("n3_cards").add([row])
    else:
        db.create_table("n3_cards", data=[row])
    return _display_path(root, db_path)
