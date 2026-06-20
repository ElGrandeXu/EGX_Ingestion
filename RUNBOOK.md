# RUNBOOK

## Start

1. Read `memory/INDEX.n3`.
2. Read relevant `memory/*.n3`.
3. Read N2 only when N3 is insufficient.
4. Read N1 only for proof, audit, license, security, tests, contradiction or explicit request.
5. Keep user output CAVEMAN final-only.

## Setup

```powershell
python -m pip install -e .
egx check
```

## Config

- Defaults: `.egxrc`.
- Env sample: `.env.example`.
- Overrides: `EGX_PROVIDER`, `EGX_MODEL`, `EGX_MODE`, `EGX_CONFIG`, `EGX_API_KEY`.

## Ingest

One source only:

```powershell
egx ingest <source> --provider openai --model default --mode caveman --export md
```

Creates:

- `sources/<source-id>.n1.md`
- `sources/<source-id>.n2.md`
- `memory/<source-id>.n3`
- `memory/exports/<source-id>-N3.md`
- `logs/ingest-*.json`

Then inspect only what can change the verdict.

## Export

```powershell
egx export <source> --format md
egx export <source> --format json
egx export <source> --format yaml
egx export <source> --format mcp
```

Optional local vector export:

```powershell
python -m pip install -e .[vector]
egx export <source> --format json --vector
```

## Observe

```powershell
egx status
egx logs --last 3
```

Logs are operational evidence only. Do not promote logs to doctrine.

## Self-Review

```powershell
egx ingest <source> --self-review
egx review --last 1
egx review --last 1 --auto-apply
```

Review cards live at `memory/self-review-*.n3`. `--auto-apply` is limited to safe minor patches.

## Repo Evidence

- Clone only when local inspection can change the verdict.
- Use `repos/<source-id>/`.
- Read setup files before commands.
- Record decision-changing commands in N2.
- Delete temporary repo evidence after synthesis unless retention is required.

## Validate

```powershell
egx check
.\scripts\check_workspace.ps1
git diff --check
git status --short
```
