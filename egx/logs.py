from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .exporter import _density, parse_n3


def _now() -> tuple[str, str]:
    dt = datetime.now().astimezone()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return dt.isoformat(timespec="seconds"), stamp


def _int(value: Any) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _card_data(root: Path, slug: str) -> dict[str, str]:
    path = root / "memory" / f"{slug}.n3"
    if not path.exists():
        return {}
    return parse_n3(path.read_text(encoding="utf-8"))


def write_ingest_log(
    root: Path,
    source: str,
    slug: str,
    config: dict[str, Any],
    result: dict[str, Any] | None,
    duration_ms: int,
    status: str = "success",
    error: str | None = None,
) -> str:
    timestamp, stamp = _now()
    data = _card_data(root, slug)
    payload: dict[str, Any] = {
        "timestamp": timestamp,
        "source": source,
        "source_slug": slug,
        "model_used": config.get("model", "default"),
        "tokens_in": _int(config.get("tokens_in")),
        "tokens_out": _int(config.get("tokens_out") or config.get("tokens")),
        "duration_ms": duration_ms,
        "verdict": (result or {}).get("verdict") or data.get("V", "WATCH"),
        "confidence": data.get("CONF", "LOW"),
        "density_score": _density(data) if data else 0,
        "next_action": (result or {}).get("next") or data.get("NEXT", "inspect-source"),
        "status": status,
    }
    if error:
        payload["error"] = error[:240]

    log_dir = root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    path = log_dir / f"ingest-{stamp}-{slug}.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path.relative_to(root).as_posix()


def ingest_log_paths(root: Path) -> list[Path]:
    log_dir = root / "logs"
    if not log_dir.exists():
        return []
    return sorted(log_dir.glob("ingest-*.json"), key=lambda path: path.stat().st_mtime, reverse=True)


def read_log(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"timestamp": path.name, "source_slug": path.stem, "status": "error", "error": str(exc)}


def recent_ingest_logs(root: Path, last: int = 5) -> list[dict[str, Any]]:
    return [read_log(path) for path in ingest_log_paths(root)[: max(0, last)]]


def format_log_lines(entries: list[dict[str, Any]]) -> list[str]:
    if not entries:
        return ["none"]
    lines: list[str] = []
    for item in entries:
        lines.append(
            "{timestamp} {source_slug} {verdict}/{confidence} d={density_score} {status} next={next_action}".format(
                timestamp=item.get("timestamp", "unknown"),
                source_slug=item.get("source_slug", "source"),
                verdict=item.get("verdict", "WATCH"),
                confidence=item.get("confidence", "LOW"),
                density_score=item.get("density_score", 0),
                status=item.get("status", "unknown"),
                next_action=item.get("next_action", "none"),
            )
        )
    return lines
