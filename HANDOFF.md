# HANDOFF

Start at `memory/INDEX.n3`.

`EGX_Ingestion` is a clean public agent-first ingestion base.

Preserved doctrine:

- CAVEMAN final-only;
- token saving;
- Memory Hierarchy Architecture;
- `N3 -> N2 -> N1`;
- one-source ingestion;
- source -> synthesis -> decision;
- agent minimalism;
- ingestion/production separation.

Current content:

- retained source notes: none;
- retained source cards: none;
- N3 exports path: `memory/exports/`;
- export formats: `md`, `json`, `yaml`, `mcp`;
- optional vector store: LanceDB via `egx export <source> --vector`;
- retained clones: none;
- active skills: `.codex/skills/`.

Next action: ingest exactly one new source with `egx ingest <source> --export md`.

After structural edits run `.\scripts\check_workspace.ps1`.
