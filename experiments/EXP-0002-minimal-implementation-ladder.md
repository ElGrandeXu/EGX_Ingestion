# EXP-0002 - Minimal implementation ladder

## Objective

Test whether the adapted Ponytail pattern should become an active EGX_Ingestion rule and a candidate EGX_Production principle.

## Source pattern

Source: `github-dietrichgebert-ponytail`.

Adapted pattern: choose the smallest useful action before adding files, scripts, dependencies, abstractions, always-on rules or production doctrine. Preserve deep work, practical experiments, documentation, registers, risk tracking and verification.

## Task tested

Improve management of `NEXT_MISSION.md` after ingestions without creating a ticket system or workflow framework.

## Ladder applied

1. Do nothing: rejected. `NEXT_MISSION.md` was clear enough for the first follow-up, but it mixed generic source-ingestion procedure with experiment follow-up and could drift longer after each source.
2. Reuse existing doctrine/template: accepted. The workspace already uses Markdown registers and templates.
3. Edit existing file first: accepted. `NEXT_MISSION.md` should carry the next-action contract.
4. Create new file only if repeated reuse is likely: accepted for one small template in `templates/`, because next-mission refresh is a recurring handoff task.
5. Script: rejected. No automation is needed.
6. New folder or registry: rejected. Existing root file and `templates/` are enough.
7. Small reversible patch: accepted.

## Options considered

- No change: too weak; leaves the known drift risk unresolved.
- Edit only `NEXT_MISSION.md`: useful, but does not preserve a reusable shape for future handoffs.
- Add `templates/next-mission-template.md`: useful and consistent with existing template practice.
- Add a next-action registry, ticket folder or script: rejected as premature framework.
- Install or activate Ponytail: rejected by mission scope and prior source decision.

## Decision

KEEP the adapted ladder as an active EGX_Ingestion rule. Use it as a small decision gate before adding structures or dependencies.

For the bounded task, patch only:

- `NEXT_MISSION.md`
- `templates/next-mission-template.md`
- theme and registry documentation
- a short pointer in `AGENTS.md`

## Patch applied

- Added `themes/agent-minimalism/minimal-implementation-ladder.md`.
- Added `templates/next-mission-template.md`.
- Reframed `NEXT_MISSION.md` around a compact next-action contract.
- Added a short AGENTS rule pointing to the ladder.
- Updated theme experiment and production files plus root registers.

## What was avoided

- No script.
- No ticket system.
- No new folder.
- No dependency.
- No global install.
- No Ponytail activation.
- No pseudo-agent framework.

## Result

The ladder produced a smaller patch than the likely overbuilt alternatives while preserving the useful outcome: future missions should have a clear next action, decision question, evidence needed and stop condition.

## Verdict

KEEP

Scores:

* Practical value: 5
* Friction reduction: 4
* Complexity added: 2
* Risk: 2
* Production relevance: 4

## Decision for EGX_Ingestion

Make `minimal-implementation-ladder` an active EGX_Ingestion rule. Keep it as a short pointer in `AGENTS.md` and detailed guidance in `themes/agent-minimalism/minimal-implementation-ladder.md`.

## Potential impact EGX_Production

Promote as a candidate EGX_Production engineering principle, not as a plugin. Re-evaluate after at least one real production-style implementation task.

