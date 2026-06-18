# RUNBOOK

Operational procedures for `EGX_Ingestion`.

## Prepare an ingestion

1. Read `AGENTS.md`, `CURRENT_STATE.md`, `INGESTION_PROTOCOL.md`, `SOURCE_INDEX.md`, `THEME_MAP.md`, `DECISIONS.md`, `PRODUCTION_CANDIDATES.md` and `RISK_REGISTER.md`.
2. Check sources from the prompt or `inbox/sources_to_ingest.md`.
3. Select exactly one source.
4. Assign a short source ID, for example `SRC-0001`.
5. Record source type as metadata, not as the primary organization axis.
6. Identify the decision question the source should answer.

## Ingest a GitHub source

1. Read the repo page, README, visible license, setup files and relevant scripts.
2. Identify the real purpose, target users, maturity and maintenance signals.
3. Determine probable theme and whether it is new, active, candidate or rejected.
4. Decide whether a clone is necessary.
5. If no clone is necessary, document the reason in the source note.
6. If a clone is necessary, follow `Decide to clone` and `Test a cloned repo`.
7. Produce the source note and all transversal updates before any next source.

## Ingest a non-GitHub source

1. Read the primary source first.
2. Identify claims, patterns, workflows, dependencies, risks and practical evidence.
3. Separate what is applicable from what is merely interesting.
4. Produce a decision-oriented source note.
5. Update theme, index, decisions, candidates, risks and experiments when relevant.

## Decide to clone

Clone only if at least one criterion is true:

- the README or docs do not allow a fair practical-value score;
- an example must be run to validate feasibility;
- code architecture may influence `EGX_Production`;
- setup scripts, dependencies or command behavior affect risk;
- provisional scoring depends on concrete inspection.

Do not clone if:

- the source is clearly rejected without local evidence;
- the repo is too large or noisy for the current decision;
- clone risk is disproportionate;
- the useful information is visible without clone;
- the current mission forbids cloning.

Record the decision in the source note.

## Test a cloned repo

1. Clone only into `repos/cloned/`.
2. Inspect README, package files, setup files, scripts, config and obvious entrypoints.
3. Before running a command, note its expected purpose and possible effects.
4. Log external-repo commands in `logs/command-log.md`.
5. Prefer read-only diagnostics before installs, builds, demos or tests.
6. Document objective, result, errors and conclusion in `EXPERIMENT_LOG.md`.
7. Keep only outputs that support a decision.

## Clean after test

1. Do not delete useful results before documenting them.
2. Move or archive only inside the workspace.
3. Signal retained clones in `SOURCE_INDEX.md`.
4. Signal pollution risk in `RISK_REGISTER.md` when needed.
5. Do not create production files from test artifacts.

## Update synthesis

After each source:

1. Add or update the source note in `sources/`.
2. Update `SOURCE_INDEX.md`.
3. Update the relevant theme in `themes/`.
4. Update `THEME_MAP.md`.
5. Add decisions to `DECISIONS.md`.
6. Add production candidates only when practical value is clear.
7. Add or update risks in `RISK_REGISTER.md`.
8. Add or update experiments in `EXPERIMENT_LOG.md`.
9. Update `CURRENT_STATE.md`, `NEXT_MISSION.md` and `HANDOFF.md` when session state changed.

## Prepare a handoff

1. State last source processed or `none`.
2. State active or candidate themes.
3. State pending decisions and blocked items.
4. List changed files.
5. Update `CURRENT_STATE.md`.
6. Update `NEXT_MISSION.md`.
7. Update `HANDOFF.md`.
8. Run `.\scripts\check_workspace.ps1`.
9. Summarize status, decisions, limits and next mission.

## Verify workspace health

Run:

```powershell
.\scripts\check_workspace.ps1
```

The script is read-only. It must check required files, non-empty required content, active skills and non-empty templates.
