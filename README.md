# EGX_Ingestion

[![Validate Workspace](https://github.com/ElGrandeXu/EGX_Ingestion/actions/workflows/validate-workspace.yml/badge.svg)](https://github.com/ElGrandeXu/EGX_Ingestion/actions/workflows/validate-workspace.yml)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License MIT](https://img.shields.io/badge/license-MIT-green)

Agent-first ingestion memory for CLI LLM power users.

One source in. N1 proof, N2 synthesis, N3 decision, export out. Built for CAVEMAN final-only work: compact memory, low token drag, no production bleed.

## Features

- Python CLI: `egx`.
- One source at a time.
- Memory route: `N3 -> N2 -> N1`.
- Outputs: N1 proof, N2 note, N3 card.
- Exports: `md`, `json`, `yaml`, `mcp`.
- Logs: compact `logs/ingest-*.json`.
- Self-review: `memory/self-review-*.n3`.
- Optional vector export: LanceDB.

## Install

```powershell
git clone https://github.com/ElGrandeXu/EGX_Ingestion.git; cd EGX_Ingestion; python -m pip install -e .; egx check
```

## Quick Use

```powershell
egx ingest https://github.com/example/repo --mode caveman --export md
egx status
egx logs --last 3
egx review --last 1
egx export repo --format json
egx check
```

## Commands

| Command | Use |
| --- | --- |
| `egx ingest <source>` | Create N1/N2/N3 and default export. |
| `egx ingest <source> --self-review` | Add compact self-review card. |
| `egx export <source> --format md|json|yaml|mcp` | Export agent-ready N3. |
| `egx export <source> --vector` | Write local LanceDB export. |
| `egx status` | Show config, card counts, recent logs. |
| `egx logs --last N` | Read recent ingest logs. |
| `egx review --last N` | Review recent ingestion health. |
| `egx check` | Validate workspace contract. |

## Config

- Defaults: `.egxrc`.
- Env sample: `.env.example`.
- Overrides: `EGX_PROVIDER`, `EGX_MODEL`, `EGX_MODE`, `EGX_CONFIG`, `EGX_API_KEY`.

## Philosophy

- CAVEMAN final-only.
- Token saving over verbosity.
- Agent-first paths and decisions.
- Memory hierarchy: `N3 -> N2 -> N1`.
- Source -> synthesis -> decision.
- Ingestion workspace, not production workspace.

## Agent Start

1. Read `AGENTS.md`.
2. Read `memory/INDEX.n3`.
3. Read relevant N3 cards.
4. Escalate to N2/N1 only when decision-changing.
5. Use `egx export <source> --format json|md|yaml|mcp` for handoff.

## License

MIT. See `LICENSE`.
