# DECISIONS

Registry of decisions produced by sources, experiments and workspace consolidation.

| Date | Source / context | Type | Decision | Reason | Impact | Next verification | Status |
|---|---|---|---|---|---|---|---|
| 2026-06-18 | Initial setup | Workspace structure | Structure `EGX_Ingestion` as a Codex-native research and decision workspace | Separate ingestion, experimentation and future production | Prepares future source-by-source ingestion without freezing `EGX_Production` | First real source ingestion | Active |
| 2026-06-18 | Quality consolidation | Skills location | Treat `.agents/skills/` as the active Codex skill location and `skills/` as documentary mirror | Official Codex skill discovery for repo skills uses `.agents/skills/`; active skills must be autosufficient | Reduces trigger ambiguity for future ingestions | Check skills frontmatter and content during workspace check | Active |

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
