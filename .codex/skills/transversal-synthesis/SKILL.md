---
name: transversal-synthesis
description: Use after each source ingestion to synchronize SOURCE_INDEX, THEME_MAP, decisions, production candidates, risks, experiments, theme files, and handoff state before any next source.
---

# Transversal Synthesis

Use after every single source. Do not skip this step, including for rejected sources.

## Inputs

- Completed source note.
- Verdict and scores.
- Clone/test result or decision not to test.
- Relevant theme files.
- Existing root registries.

## Required updates

1. `SOURCE_INDEX.md`: add the source row with verdict, scores, note path, clone status and experiment link.
2. Theme folder: create or update sources, patterns, decisions, experiments, production implications and cross-links as needed.
3. `THEME_MAP.md`: update theme maturity, candidate/active/rejected status, links and production implication.
4. `DECISIONS.md`: add concrete decisions or mark no new decision when appropriate.
5. `PRODUCTION_CANDIDATES.md`: add only items with clear practical value, risk notes and next test.
6. `RISK_REGISTER.md`: add or update risks when risk exists or changes.
7. `EXPERIMENT_LOG.md`: add tests run or proposed for `TEST` verdicts.
8. `CURRENT_STATE.md`, `NEXT_MISSION.md`, `HANDOFF.md`: update when state, next action or blocker changed.

## Quality bar

- Keep entries short but decision-oriented.
- Do not add production candidates for novelty alone.
- Do not hide uncertainty; convert it into a test, watch item or rejection reason.
- Keep source type as metadata and theme as the organizing axis.

## Output

- All relevant registries synchronized.
- Explicit next action for the next source, experiment or user decision.
- No fake placeholder source left in registries.
