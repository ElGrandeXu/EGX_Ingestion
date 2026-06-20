# EGX_Ingestion Agent Instructions

Purpose: public, agent-first template for ingesting one technical or methodological source at a time.

This workspace is not production. Do not create or modify production workspaces unless explicitly asked.

## First Read

1. `memory/INDEX.n3`
2. Relevant N3 cards.
3. N2 only when N3 is insufficient.
4. N1 only for new ingestion, audit, license, security, tests, contradiction or explicit request.

Doctrine: `N3 -> N2 -> N1`.

## Rules

- Default communication is CAVEMAN final-only.
- Use `.codex/skills/caveman-final-only` for final-only, CAVEMAN or token saving.
- Speak before final only for authentication, private material, destructive action outside this workspace, permission, irreversible ambiguity or total blocker.
- Process exactly one source at a time.
- Every source produces N1 proof, one N2 note and one N3 card at `memory/<source-id>.n3`.
- Every ingestion exports `memory/exports/<source-id>-N3.md`.
- Use `egx export <source> --format json|md|yaml|mcp` for agent handoff.
- Use `repos/<source-id>/` for temporary repo evidence; delete it after synthesis unless retention is required.
- Read setup files and scripts before external-repo commands.
- Record decision-changing external commands in N2.
- Prefer `egx check`; it delegates to `scripts/check_workspace.ps1`.
- Use `egx status` and `egx logs --last N` before rereading N2/N1.
- Treat `logs/ingest-*.json` as operational evidence, not doctrine.
- Use `egx review --last N` or `egx ingest <source> --self-review` for self-improvement cards.

## Canon

Active doctrine:

- `doctrine/CORE.md`
- `doctrine/MEMORY_HIERARCHY.md`
- `doctrine/INGESTION.md`

Preserve CAVEMAN, token saving, Memory Hierarchy Architecture, `N3 -> N2 -> N1`, source -> synthesis -> decision, agent minimalism and ingestion/production separation.

Everything else is disposable when it does not improve future agent decisions.
