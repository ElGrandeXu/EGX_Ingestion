# Minimal Implementation Ladder

Status: active EGX_Ingestion rule, candidate EGX_Production principle.

Use this ladder before adding files, scripts, dependencies, abstractions or doctrine.

## Ladder

1. Do nothing if the current evidence does not require an action.
2. Reuse existing workspace doctrine, registers and templates before creating new structures.
3. Prefer editing an existing file over creating a new one.
4. Prefer Markdown decision records over scripts when no repeatable automation is needed.
5. Prefer built-in shell, Git and PowerShell over new dependencies.
6. Prefer local contained experiments over global installs.
7. Prefer the smallest reversible patch that makes the next action clearer.
8. Add an abstraction only after repeated need is visible in the workspace.
9. Add a dependency only with explicit practical gain and recorded risk.
10. Promote anything to `EGX_Production` only after source evidence, experiment evidence and a decision record.

## Not Lazy About

- Reading required files.
- Practical experiments.
- Source notes and scoring.
- Register synchronization.
- Risk tracking.
- Verification.
- Clear next actions.

## Test Trigger

Use the ladder when a mission might create a new framework layer, script, folder, template, skill, dependency or production candidate.

## Stop Condition

If the useful patch is just a short Markdown edit, stop there. Do not add automation until the same manual step repeats and costs more than the script would save.

