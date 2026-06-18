---
name: repo-lab-test
description: Use when a GitHub source needs a contained clone, local inspection, command review, or bounded practical test before a source verdict can be trusted.
---

# Repo Lab Test

Documentary mirror of the active skill in `.agents/skills/repo-lab-test/SKILL.md`.

Use only when a practical repository check can change the source decision.

## Scope rules

- Stay inside `C:\Users\maxer\Desktop\EGX_Ingestion`.
- Clone only into `repos/cloned/`.
- Do not install dependencies unless the current mission permits it and the source decision requires it.
- Read setup files and scripts before running commands from the repo.
- Prefer read-only diagnostics before builds, demos, installs or tests.
- Log external-repo commands in `logs/command-log.md`.
- Record experiment conclusions in `EXPERIMENT_LOG.md`.

## Clone/test gate

Before cloning or running a command, state:

- decision question;
- why source reading is insufficient;
- expected signal;
- risk;
- stop condition.

Skip clone/test if it will not change the verdict.

## Steps

1. Confirm the source ID and linked source note.
2. State why clone or local inspection is necessary.
3. Clone into `repos/cloned/` only when allowed by the mission.
4. Inspect README, license, package files, setup files, scripts, config and obvious entrypoints.
5. Identify risky commands, network behavior, generated outputs and dependency footprints.
6. Run only commands that answer the decision question.
7. Log each command with date, cwd, purpose, result and risk notes.
8. Update `EXPERIMENT_LOG.md` with objective, result, errors, conclusion and verdict impact.
9. Update the source note with practical findings.

## Output

- Command log entry if any external-repo command ran.
- Experiment log entry or explicit "inspection only" note.
- Decision impact for source verdict and scores.
- Risk register update when needed.
