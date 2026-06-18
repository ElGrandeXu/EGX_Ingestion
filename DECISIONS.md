# DECISIONS

Registry of decisions produced by sources, experiments and workspace consolidation.

| Date | Source / context | Type | Decision | Reason | Impact | Next verification | Status |
|---|---|---|---|---|---|---|---|
| 2026-06-18 | Initial setup | Workspace structure | Structure `EGX_Ingestion` as a Codex-native research and decision workspace | Separate ingestion, experimentation and future production | Prepares future source-by-source ingestion without freezing `EGX_Production` | First real source ingestion | Active |
| 2026-06-18 | Quality consolidation | Skills location | Treat `.agents/skills/` as the active Codex skill location and `skills/` as documentary mirror | Earlier official Codex skill discovery signal used `.agents/skills/`; active skills had to be autosufficient | Historical decision replaced by Caveman doctrine path decision | `CAVEMAN_AUDIT.md` | Superseded |
| 2026-06-18 | Caveman doctrine | Communication | Default user-visible communication is final-only | Saves tokens without reducing analysis, tests, audits or register updates | Future missions write detail into files and return compressed final only | `scripts/check_workspace.ps1` doctrine checks | Active |
| 2026-06-18 | Caveman doctrine | Skills location | Treat `.codex/skills/` as primary repo-scoped Codex skill location; keep `.agents/skills/` as compatibility mirror | Current mission and Codex changelog support `.codex/skills`; existing workspace/session still had `.agents/skills` discovery signals | Preserves current skill behavior while aligning forward architecture | Check both paths and mirror status in `scripts/check_workspace.ps1` | Active |

## Decision types

- `Workspace structure`
- `Source verdict`
- `Theme evolution`
- `Production candidate`
- `Experiment`
- `Risk mitigation`

## Status values

- `Active`: decision in force.
- `To test`: needs a practical experiment.
- `Superseded`: replaced by a newer decision.
- `Archived`: kept for history.
- `Rejected`: explicitly not adopted.
