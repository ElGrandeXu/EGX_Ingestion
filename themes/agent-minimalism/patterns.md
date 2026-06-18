# Patterns

## Keep

- Ask whether the requested code needs to exist before writing it.
- Prefer standard library functionality before custom code.
- Prefer native platform features before dependencies.
- Reuse already-installed dependencies before adding new ones.
- Keep the smallest implementation that satisfies the current requirement.
- Delete or avoid speculative abstractions.
- Leave one runnable check for non-trivial logic.

## Adapt

- Use a local EGX wording for the ladder instead of importing Ponytail persona text.
- Track intentional shortcuts with a ceiling and an upgrade trigger.
- Use review/audit mode before any always-on instruction mode.
- Apply the ladder to future production implementation tasks, not to ingestion notes.
- For EGX_Ingestion, apply `minimal-implementation-ladder.md` before adding scripts, folders, dependencies, new registers or production candidates.

## Test

- Compare normal implementation vs adapted minimalism checklist on one bounded coding task.
- Measure files changed, dependencies added, validation retained and tests/checks retained.
- Check whether minimalism reduces code without increasing rework.

## Reject

- Installing Ponytail as a plugin in this workspace.
- Always-on hook injection before a local test proves value.
- Treating line count as success when validation, security or accessibility are removed.
- Copying multi-agent adapter trees into `EGX_Ingestion`.
