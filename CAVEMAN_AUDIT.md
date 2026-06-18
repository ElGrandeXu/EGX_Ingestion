# CAVEMAN_AUDIT

Date: 2026-06-18

## Current state

- `AGENTS.md` existed and defined end-of-mission reporting, but the requested final response was verbose.
- `README.md`, `RUNBOOK.md`, `INGESTION_PROTOCOL.md`, `CURRENT_STATE.md`, `NEXT_MISSION.md`, `HANDOFF.md`, `QUALITY_AUDIT.md`, `PATCH_PLAN.md` and `GIT_PUBLISH_AUDIT.md` were read.
- `.codex/` was absent.
- `.agents/skills/` existed with active workspace skills: `source-ingestion`, `repo-lab-test`, `transversal-synthesis`.
- `skills/` existed as documentary mirror for the same three skills.
- Existing skills had `SKILL.md` with `name` and `description` frontmatter.

## Token waste problem

The workspace required rigorous file updates, source notes, registers and handoff, but it also encouraged visible progress narration and long final reports. That wastes user-visible tokens without improving analysis, tests or decisions.

Target doctrine:

- big reasoning;
- small visible output;
- final-only by default;
- interruption only for real blockers.

## Sources checked

- OpenAI `AGENTS.md` guide: Codex reads `AGENTS.md` before work, layers project instructions from repo root to current directory, and uses closer files as later overrides.
- OpenAI skills guide: skills are folders with required `SKILL.md`; frontmatter needs `name` and `description`; implicit triggering depends on `description`.
- OpenAI Codex changelog: Codex CLI/IDE skills support is documented, including per-user `~/.codex/skills` and per-repo `.codex/skills`.
- Current OpenAI skills page also mentions repository scanning under `.agents/skills`; this conflicts with the changelog wording.
- Caveman source: output compression preserves technical accuracy and reasoning while reducing visible reply tokens.

## Skill paths

Observed:

- `.codex/skills/`: absent before this mission.
- `.agents/skills/`: active in this current workspace/session; already referenced by existing docs.
- `skills/`: documentary mirror.

Decision:

- `.codex/skills/` is the recommended Codex repo-scoped home going forward, per current mission and changelog signal.
- `.agents/skills/` remains compatibility/history mirror because this workspace already uses it and current skill discovery may still read it.
- `skills/` remains human documentation and non-priority mirror.

## Modifications proposed

- Create `.codex/skills/` and add `caveman-final-only`.
- Copy existing active skills into `.codex/skills/` to avoid losing ingestion behavior.
- Keep `.agents/skills/` and add a compatibility mirror of `caveman-final-only`.
- Update `AGENTS.md` and protocols to make `COMMUNICATION_PROTOCOL.md` the communication source of truth.
- Update `scripts/check_workspace.ps1` to verify the doctrine and skill placement.

## Risks

- OpenAI docs currently show both `.agents/skills` and `.codex/skills` depending on page/changelog. Keeping both avoids breakage.
- Duplicate skill names can appear if a future Codex version scans both locations. If that happens, keep `.codex/skills/` and disable or remove mirrors only after explicit mission approval.
- Final-only can hide useful progress if a task is genuinely blocked; exceptions are defined in `COMMUNICATION_PROTOCOL.md`.

## Decisions

- Adopt final-only user communication by default.
- Preserve all internal rigor, tests, file updates and ingestion obligations.
- Make `.codex/skills/` primary for repo-scoped Codex skills.
- Keep `.agents/skills/` as compatibility mirror.
- Keep `skills/` as human documentation.
