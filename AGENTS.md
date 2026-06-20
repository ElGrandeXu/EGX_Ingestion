# EGX_Ingestion Agent Instructions

Purpose: public, agent-first template for ingesting one technical or methodological source at a time.

This workspace is not production. Do not create or modify production workspaces unless a later mission explicitly asks for it.

## First Read

1. `memory/INDEX.n3`
2. Relevant N3 cards, when present.
3. N2 synthesis only when N3 is insufficient.
4. N1 proof only for new ingestion, audit, license, security, tests, contradiction or explicit request.

Doctrine: `N3 -> N2 -> N1`.

## Operating Rules

- Default communication is CAVEMAN final-only.
- Use `.codex/skills/caveman-final-only` when final-only, CAVEMAN or token saving is requested.
- Speak before final only for authentication, private material, destructive action outside this workspace, permission, irreversible ambiguity or total blocker.
- Process exactly one source at a time.
- Every source produces N1 proof, one N2 note and one N3 card in `memory/<source-id>.n3`.
- Temporary repo evidence belongs under `repos/<source-id>/` and is deleted after synthesis unless retention is explicitly required.
- Read setup files and scripts before external-repo commands.
- Record external commands in the N2 note when clone or test evidence affects the decision.
- Canonical repo-scoped skills live only in `.codex/skills/`.

## Canon

Active doctrine:

- `doctrine/CORE.md`
- `doctrine/MEMORY_HIERARCHY.md`
- `doctrine/INGESTION.md`

Preserve CAVEMAN, token saving, Memory Hierarchy Architecture, `N3 -> N2 -> N1`, source -> synthesis -> decision, agent minimalism and ingestion/production separation.

Everything else is disposable when it does not improve future agent decisions.
