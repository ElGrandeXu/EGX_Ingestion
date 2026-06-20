from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .exporter import export_card, update_index_ref
from .logs import ingest_log_paths, recent_ingest_logs


def _slug() -> str:
    return "self-review-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ").lower()


def _safe(value: str, fallback: str, size: int = 48) -> str:
    clean = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
    return (clean[:size].strip("-") or fallback)


def _collect_output_text(data: dict[str, Any]) -> str:
    if isinstance(data.get("output_text"), str):
        return data["output_text"]
    parts: list[str] = []
    for item in data.get("output", []) or []:
        for content in item.get("content", []) or []:
            if content.get("type") == "output_text" and content.get("text"):
                parts.append(str(content["text"]))
    return "\n".join(parts).strip()


def _parse_json(text: str) -> dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end])
            except json.JSONDecodeError:
                pass
    return {
        "verdict": "WATCH",
        "confidence": "LOW",
        "next_action": "review-manually",
        "suggestions": [text[:300] if text else "No parseable review output."],
        "patch_target": "none",
        "patch_summary": "manual review required",
        "why": "provider-output-not-json",
    }


def _choice(value: Any, allowed: set[str], fallback: str) -> str:
    text = str(value or fallback).upper()
    return text if text in allowed else fallback


def _suggestions(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item)[:240] for item in value if str(item).strip()][:5] or ["no-change"]
    if isinstance(value, str) and value.strip():
        return [value[:240]]
    return ["no-change"]


def _normalize(review: dict[str, Any]) -> dict[str, Any]:
    return {
        "verdict": _choice(review.get("verdict"), {"APPLY", "WATCH", "REJECT"}, "WATCH"),
        "confidence": _choice(review.get("confidence"), {"LOW", "MED", "HIGH"}, "LOW"),
        "next_action": _safe(str(review.get("next_action", "review-manually")), "review-manually"),
        "suggestions": _suggestions(review.get("suggestions")),
        "patch_target": str(review.get("patch_target", "none"))[:120] or "none",
        "patch_summary": str(review.get("patch_summary", "none"))[:240] or "none",
        "why": _safe(str(review.get("why", "self-review")), "self-review"),
    }


def _context(root: Path, entries: list[dict[str, Any]]) -> str:
    cards: list[dict[str, str]] = []
    for entry in entries:
        slug = str(entry.get("source_slug", ""))
        path = root / "memory" / f"{slug}.n3"
        if path.exists():
            cards.append({"path": path.relative_to(root).as_posix(), "text": path.read_text(encoding="utf-8").strip()})
    return json.dumps({"logs": entries, "cards": cards}, ensure_ascii=False)


def _openai_review(config: dict[str, Any], prompt: str) -> tuple[dict[str, Any] | None, dict[str, int], str | None]:
    if config.get("provider", "openai") != "openai" or not os.getenv("EGX_API_KEY"):
        return None, {"tokens_in": 0, "tokens_out": 0}, "provider-unavailable"
    model = config.get("model", "default")
    if model == "default":
        model = "gpt-4.1"
    body = {
        "model": model,
        "instructions": (
            "Review EGX ingestion observability. Output compact JSON only with keys: "
            "verdict APPLY|WATCH|REJECT, confidence LOW|MED|HIGH, next_action, "
            "suggestions array, patch_target, patch_summary, why. Use patch_target "
            "memory/INDEX.n3 only for missing log/review routes. Be CAVEMAN compact."
        ),
        "input": prompt,
        "max_output_tokens": 500,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {os.environ['EGX_API_KEY']}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return None, {"tokens_in": 0, "tokens_out": 0}, str(exc)
    usage = data.get("usage") or {}
    review = _parse_json(_collect_output_text(data))
    return review, {"tokens_in": int(usage.get("input_tokens") or 0), "tokens_out": int(usage.get("output_tokens") or 0)}, None


def _local_review(entries: list[dict[str, Any]], provider_note: str | None) -> dict[str, Any]:
    if not entries:
        return {
            "verdict": "WATCH",
            "confidence": "LOW",
            "next_action": "run-ingest-with-log",
            "suggestions": ["Run egx ingest <source> --log before review."],
            "patch_target": "none",
            "patch_summary": "none",
            "why": provider_note or "no-ingest-log",
        }
    latest = entries[0]
    if latest.get("status") == "error":
        verdict, next_action, why = "APPLY", "inspect-error-log", "latest-ingest-error"
    elif int(latest.get("density_score") or 0) < 70:
        verdict, next_action, why = "APPLY", "raise-n3-density", "low-density"
    elif latest.get("confidence") == "LOW":
        verdict, next_action, why = "WATCH", "inspect-source", "low-confidence"
    else:
        verdict, next_action, why = "REJECT", "no-change", "healthy-ingestion"
    note = f"; {provider_note}" if provider_note else ""
    return {
        "verdict": verdict,
        "confidence": "MED" if verdict != "REJECT" else "HIGH",
        "next_action": next_action,
        "suggestions": [f"{next_action} for {latest.get('source_slug', 'source')}{note}"],
        "patch_target": "none",
        "patch_summary": "none",
        "why": why,
    }


def _card(slug: str, log_path: str, review: dict[str, Any]) -> str:
    verdict = review["verdict"]
    n3_verdict = "ADAPT" if verdict == "APPLY" else verdict if verdict in {"WATCH", "REJECT"} else "WATCH"
    return "\n".join(
        [
            f"ID={slug}",
            "TYPE=decision",
            f"V={n3_verdict}",
            "TH=observability",
            "RISK=LOW",
            "PROD=NO",
            f"CONF={review['confidence']}",
            "N2=none",
            f"N1={log_path or 'none'}",
            f"NEXT={review['next_action']}",
            f"WHY={review['why']}",
            "",
        ]
    )


def _apply_minor(root: Path, review: dict[str, Any], auto_apply: bool) -> str:
    if not auto_apply:
        return "off"
    if review["verdict"] != "APPLY":
        return "skipped-verdict"
    if review["patch_target"].replace("\\", "/") != "memory/INDEX.n3":
        return "skipped-no-safe-patch"
    index = root / "memory" / "INDEX.n3"
    text = index.read_text(encoding="utf-8") if index.exists() else ""
    additions = [line for line in ("LOGS=logs/ingest-*.json", "SELF_REVIEW=memory/self-review-*.n3") if line not in text]
    if not additions:
        return "already-present"
    index.write_text(text.rstrip() + "\n" + "\n".join(additions) + "\n", encoding="utf-8")
    return "applied-index-routes"


def review_ingestions(root: Path, config: dict[str, Any], last: int = 1, auto_apply: bool = False) -> dict[str, Any]:
    entries = recent_ingest_logs(root, last)
    provider_review, usage, provider_note = _openai_review(config, _context(root, entries))
    review = _normalize(provider_review or _local_review(entries, provider_note))
    slug = _slug()
    paths = ingest_log_paths(root)
    log_path = paths[0].relative_to(root).as_posix() if paths else "none"
    path = root / "memory" / f"{slug}.n3"
    path.write_text(_card(slug, log_path, review), encoding="utf-8")
    update_index_ref(root, slug)
    exported = export_card(root, slug, config, "md")
    applied = _apply_minor(root, review, auto_apply)
    return {
        "status": "OK",
        "review": path.relative_to(root).as_posix(),
        "export": exported,
        "verdict": review["verdict"],
        "confidence": review["confidence"],
        "suggestions": review["suggestions"],
        "patch_target": review["patch_target"],
        "patch_summary": review["patch_summary"],
        "auto_apply": applied,
        "tokens_in": usage["tokens_in"],
        "tokens_out": usage["tokens_out"],
    }
