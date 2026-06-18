# NEXT_MISSION

## Recommended next mission

Ingest the next single source, or run one production-style implementation experiment using `minimal-implementation-ladder`.

## Decision question

For a new source: what should be kept, adapted, tested, watched or rejected?

For the next experiment: does the active ladder improve a real implementation task without cutting evidence, tests or safety?

## Evidence needed

- For source ingestion: one URL, source note, verdict, scores, theme updates and transversal registers.
- For implementation experiment: task, baseline expectation, patch, avoided complexity and verification.

## Allowed changes

- Existing source, theme, register, handoff and template files.
- New source note only for a new source.
- New experiment note only for a real experiment.

## Avoid

- Batch ingestion.
- Ticket system.
- New workflow folder.
- Script or dependency unless repeated manual work proves automation value.
- Plugin install or global configuration change.

## Done when

- One source or one experiment is complete.
- `SOURCE_INDEX.md` or `EXPERIMENT_LOG.md` is updated as applicable.
- `THEME_MAP.md`, `DECISIONS.md`, `CURRENT_STATE.md`, `HANDOFF.md` and this file reflect the next action.
- `.\scripts\check_workspace.ps1` passes.

## Current blockers

- None.

## Last completed work

- `EXP-0002`: minimal implementation ladder tested and promoted to active EGX_Ingestion rule.
- Previous source: `github-dietrichgebert-ponytail`, verdict `ADAPT`, theme `agent-minimalism`.
