from __future__ import annotations

from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from .exporter import export_card, update_index_ref


def source_id(source: str) -> str:
    parsed = urlparse(source)
    raw = Path(parsed.path or source).stem or parsed.netloc or "source"
    clean = "".join(ch.lower() if ch.isalnum() else "-" for ch in raw).strip("-")
    return clean[:48] or "source"


def source_kind(source: str) -> str:
    parsed = urlparse(source)
    path = Path(source)

    if parsed.scheme in {"http", "https"} and "github.com" in parsed.netloc.lower():
        return "github"
    if parsed.scheme in {"http", "https"}:
        return "url"
    if path.suffix.lower() == ".pdf":
        return "pdf"
    if path.exists():
        return "local"
    return "unknown"


def _date() -> str:
    return datetime.now().astimezone().date().isoformat()


def _write_if_missing(root: Path, path: Path, text: str, created: list[str]) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    created.append(path.relative_to(root).as_posix())


def _n1_text(slug: str, source: str, kind: str) -> str:
    return f"""# N1 Source Proof

ID: {slug}
Source: {source}
Type: {kind}
Captured: {_date()}
License: unknown

## Raw Proof

- Source pointer only.

## Commands

- egx ingest {source}

## Files Or URLs

- {source}
"""


def _n2_text(slug: str, source: str, kind: str) -> str:
    return f"""# N2 Decision Note

ID: {slug}
Source: {source}
Date: {_date()}
N1: sources/{slug}.n1.md
N3: memory/{slug}.n3

## Question

- Should this source enter EGX memory?

## Evidence

- CLI source pointer captured. No external inspection yet.

## Decision

Verdict: WATCH
Risk: MED
Confidence: LOW
Production impact: MAYBE

## Keep

- Source pointer and route.

## Reject

- No unverified claims imported.

## Commands That Changed The Decision

- none

## Next

- inspect-source
"""


def _n3_text(slug: str, kind: str) -> str:
    return "\n".join(
        [
            f"ID={slug}",
            "TYPE=source",
            "V=WATCH",
            f"TH={kind}",
            "RISK=MED",
            "PROD=MAYBE",
            "CONF=LOW",
            f"N2=sources/{slug}.n2.md",
            f"N1=sources/{slug}.n1.md",
            "NEXT=inspect-source",
            "WHY=cli-ingest-pointer-only",
            "",
        ]
    )


def ingest_source(source: str, config: dict[str, str], export_format: str = "md") -> dict[str, object]:
    root = Path.cwd()
    slug = source_id(source)
    kind = source_kind(source)
    created: list[str] = []
    index = root / "memory" / "INDEX.n3"
    index_text = index.read_text(encoding="utf-8") if index.exists() else ""
    duplicate = (root / "memory" / f"{slug}.n3").exists() or f"REF=memory/{slug}.n3" in index_text

    _write_if_missing(root, root / "sources" / f"{slug}.n1.md", _n1_text(slug, source, kind), created)
    _write_if_missing(root, root / "sources" / f"{slug}.n2.md", _n2_text(slug, source, kind), created)
    _write_if_missing(root, root / "memory" / f"{slug}.n3", _n3_text(slug, kind), created)
    update_index_ref(root, slug)
    exported = export_card(root, source, config, export_format)

    return {
        "status": "OK",
        "source": source,
        "kind": kind,
        "verdict": "WATCH",
        "n3": f"memory/{slug}.n3",
        "export": exported,
        "created": created,
        "duplicate": duplicate,
        "next": "merge-duplicate" if duplicate else "inspect-source",
    }
