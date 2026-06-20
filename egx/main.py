from __future__ import annotations

from pathlib import Path
from time import perf_counter
from typing import Optional

import typer

from .check import run_workspace_check
from .config import load_config
from .exporter import export_card, export_vector
from .ingest import ingest_source, source_id
from .logs import format_log_lines, ingest_log_paths, recent_ingest_logs, write_ingest_log
from .review import review_ingestions

app = typer.Typer(no_args_is_help=True, help="EGX minimal agent-first CLI.")


def emit(items: dict[str, object]) -> None:
    for key, value in items.items():
        if isinstance(value, list):
            typer.echo(f"{key}:")
            for item in value:
                typer.echo(f"- {item}")
        else:
            typer.echo(f"{key}: {value}")


def _config(config: Optional[Path], provider: Optional[str] = None, model: Optional[str] = None, mode: Optional[str] = None) -> dict[str, str]:
    return load_config(config, {"provider": provider, "model": model, "mode": mode})


@app.command()
def ingest(
    source: str = typer.Argument(..., help="GitHub URL, local path, PDF, or source URL."),
    provider: Optional[str] = typer.Option(None, "--provider", help="Runtime provider."),
    model: Optional[str] = typer.Option(None, "--model", help="Runtime model."),
    mode: Optional[str] = typer.Option(None, "--mode", help="caveman, full, or review."),
    export_format: Optional[str] = typer.Option(None, "--export", help="Post-ingest export format: md, json, yaml, or mcp."),
    write_log: bool = typer.Option(True, "--log/--no-log", help="Write compact ingest log."),
    self_review: bool = typer.Option(False, "--self-review", help="Review latest ingestion after logging."),
    auto_apply: bool = typer.Option(False, "--auto-apply", help="Apply only safe minor review changes."),
    check: bool = typer.Option(False, "--check", help="Run only workspace check."),
    config: Optional[Path] = typer.Option(None, "--config", help="Path to .egxrc/config.yaml."),
) -> None:
    cfg = _config(config, provider, model, mode)
    if check:
        code, output = run_workspace_check(cfg)
        typer.echo(output)
        raise typer.Exit(code)
    root = Path.cwd()
    slug = source_id(source)
    start = perf_counter()
    try:
        result = ingest_source(source, cfg, export_format or cfg.get("export_format", "md"))
        duration = int((perf_counter() - start) * 1000)
        if write_log:
            status = "warning" if result.get("duplicate") else "success"
            result["log"] = write_ingest_log(root, source, slug, cfg, result, duration, status)
        if self_review:
            review = review_ingestions(root, cfg, 1, auto_apply)
            result.update({f"review_{key}": value for key, value in review.items()})
        emit(result)
    except Exception as exc:
        duration = int((perf_counter() - start) * 1000)
        failure: dict[str, object] = {"status": "FAILED", "error": str(exc)}
        if write_log:
            failure["log"] = write_ingest_log(root, source, slug, cfg, None, duration, "error", str(exc))
        emit(failure)
        raise typer.Exit(1)


@app.command()
def check(config: Optional[Path] = typer.Option(None, "--config", help="Path to .egxrc/config.yaml.")) -> None:
    cfg = load_config(config)
    code, output = run_workspace_check(cfg)
    typer.echo(output)
    raise typer.Exit(code)


@app.command()
def status(config: Optional[Path] = typer.Option(None, "--config", help="Path to .egxrc/config.yaml.")) -> None:
    cfg = load_config(config)
    root = Path.cwd()
    source_dir = root / "sources"
    sources = [path for path in source_dir.glob("*") if path.name != ".gitkeep"] if source_dir.exists() else []
    recent = recent_ingest_logs(root, 5)
    emit(
        {
            "status": "READY",
            "config": cfg["config_path"],
            "provider": cfg["provider"],
            "model": cfg["model"],
            "mode": cfg["mode"],
            "api_key": cfg["api_key"],
            "n3_cards": len(list((root / "memory").glob("*.n3"))),
            "source_notes": len(sources),
            "ingest_logs": len(ingest_log_paths(root)),
            "last_ingestions": format_log_lines(recent),
        }
    )


@app.command("logs")
def logs_cmd(last: int = typer.Option(5, "--last", min=1, help="Number of recent ingest logs.")) -> None:
    emit({"logs": format_log_lines(recent_ingest_logs(Path.cwd(), last))})


@app.command()
def review(
    last: int = typer.Option(1, "--last", min=1, help="Number of recent ingest logs to review."),
    auto_apply: bool = typer.Option(False, "--auto-apply", help="Apply only safe minor review changes."),
    config: Optional[Path] = typer.Option(None, "--config", help="Path to .egxrc/config.yaml."),
) -> None:
    emit(review_ingestions(Path.cwd(), load_config(config), last, auto_apply))


@app.command()
def export(
    source: Optional[str] = typer.Argument(None, help="Source URL, slug, or memory/<id>.n3."),
    fmt: str = typer.Option("md", "--format", "-f", help="md, json, yaml, or mcp."),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Write exported N3 text."),
    vector: bool = typer.Option(False, "--vector", help="Also export to local LanceDB."),
    config: Optional[Path] = typer.Option(None, "--config", help="Path to .egxrc/config.yaml."),
) -> None:
    cfg = load_config(config)
    root = Path.cwd()
    if source:
        try:
            exported = export_card(root, source, cfg, fmt, output)
            result: dict[str, object] = {"status": "OK", "exported": exported}
            if vector:
                result["vector"] = export_vector(root, source, cfg)
            emit(result)
        except (RuntimeError, ValueError, FileNotFoundError) as exc:
            emit({"status": "FAILED", "error": str(exc)})
            raise typer.Exit(1)
    elif output:
        chunks = [path.read_text(encoding="utf-8").strip() for path in sorted(root.glob("memory/*.n3"))]
        output.write_text("\n\n---\n\n".join(chunks) + "\n", encoding="utf-8")
        emit({"status": "OK", "exported": str(output)})
    else:
        chunks = [path.read_text(encoding="utf-8").strip() for path in sorted(root.glob("memory/*.n3"))]
        text = "\n\n---\n\n".join(chunks)
        typer.echo(text)


if __name__ == "__main__":
    app()
