# CURRENT_STATE

Date: 2026-06-21

State: clean public agent-first ingestion template with native N3 export.

## Active Surfaces

- Instructions: `AGENTS.md`
- Runbook: `RUNBOOK.md`
- Doctrine: `doctrine/`
- First read: `memory/INDEX.n3`
- N3 format: `memory/FORMAT.n3.md`
- N3 exports: `memory/exports/`
- Skills: `.codex/skills/`
- Templates: `templates/`
- Future N2 source notes: `sources/`
- Temporary N1 repo evidence: `repos/`

## State

- CAVEMAN, token saving, MHA, `N3 -> N2 -> N1`, one-source ingestion and agent minimalism preserved.
- `egx ingest` creates N1/N2/N3 scaffolds, updates `memory/INDEX.n3`, and exports compact N3.
- `egx export <source> --format md|json|yaml|mcp` supports agent handoff; `--vector` is optional LanceDB.
- Historical source notes, experiments, audits and clone artifacts removed.
- Retained local clones: none.
- Active source notes: none.
- Active production candidates: none.

## Next

Ingest one new source from a clean base, then use `egx export <source> --format json` for handoff.
