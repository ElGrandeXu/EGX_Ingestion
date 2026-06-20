from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


DEFAULTS: dict[str, str] = {
    "provider": "openai",
    "model": "default",
    "mode": "caveman",
    "workspace_check": "scripts/check_workspace.ps1",
    "export_format": "md",
}

ENV_MAP = {
    "provider": "EGX_PROVIDER",
    "model": "EGX_MODEL",
    "mode": "EGX_MODE",
}


def load_config(path: Path | None = None, overrides: dict[str, Any] | None = None) -> dict[str, Any]:
    config_path = path or Path(os.getenv("EGX_CONFIG", ".egxrc"))
    if not config_path.is_absolute():
        config_path = Path.cwd() / config_path

    data: dict[str, Any] = dict(DEFAULTS)
    if config_path.exists():
        loaded = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        if not isinstance(loaded, dict):
            raise ValueError(f"Config must be a mapping: {config_path}")
        data.update({str(k): v for k, v in loaded.items() if v is not None})

    for key, env_name in ENV_MAP.items():
        if os.getenv(env_name):
            data[key] = os.environ[env_name]

    if overrides:
        data.update({k: v for k, v in overrides.items() if v is not None})

    data["config_path"] = str(config_path) if config_path.exists() else "none"
    data["api_key"] = "set" if os.getenv("EGX_API_KEY") else "missing"
    return data
