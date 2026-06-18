# Compatibility repo skills

`.codex/skills/` is the primary repo-scoped Codex skill location for `EGX_Ingestion`.

This `.agents/skills/` directory is kept as a compatibility / historical mirror because some Codex versions and current sessions may still discover repository skills here. The top-level `skills/` folder is a documentary mirror and registry, not the source that should drive Codex behavior when content diverges.

Compatibility mirrors:

- `caveman-final-only`
- `source-ingestion`
- `repo-lab-test`
- `transversal-synthesis`

Maintenance rule: update `.codex/skills/` first. Mirror here only to avoid breaking older discovery paths.
