from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def _resolve_script(root: Path, script: str) -> Path:
    path = Path(script)
    if path.is_absolute():
        return path
    local = root / path
    if local.exists():
        return local
    return Path(__file__).resolve().parents[1] / path


def _python_fallback(root: Path) -> tuple[int, str]:
    required = [
        "AGENTS.md",
        "README.md",
        "RUNBOOK.md",
        "doctrine/CORE.md",
        "doctrine/MEMORY_HIERARCHY.md",
        "doctrine/INGESTION.md",
        "memory/INDEX.n3",
        "scripts/check_workspace.ps1",
    ]
    missing = [path for path in required if not (root / path).exists()]
    if missing:
        return 1, "Status: FAILED\n" + "\n".join(f"- Missing file: {path}" for path in missing)
    return 0, "Status: OK\nFallback: python"


def run_workspace_check(config: dict[str, str] | None = None, root: Path | None = None) -> tuple[int, str]:
    root = root or Path.cwd()
    script = _resolve_script(root, (config or {}).get("workspace_check", "scripts/check_workspace.ps1"))
    shell = shutil.which("pwsh") or shutil.which("powershell")

    if script.exists() and shell:
        result = subprocess.run(
            [shell, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script)],
            cwd=root,
            capture_output=True,
            text=True,
        )
        output = (result.stdout + result.stderr).strip()
        return result.returncode, output

    return _python_fallback(root)
