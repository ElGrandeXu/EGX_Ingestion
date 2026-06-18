# NEXT_MISSION

## Recommended next mission

Run the proposed `agent-minimalism` experiment or ingest the next single source.

The user can provide a single URL or a list of URLs. Codex must process the first unprocessed source completely before moving to the next.

Alternative experiment mission: choose one bounded implementation task and compare normal Codex behavior against an adapted minimal implementation ladder derived from Ponytail, measuring files changed, dependencies added, validation retained and checks retained.

Use final-only communication. Do not send checkpoints. Write all detailed synthesis into workspace files.

## Prompt format for user

```md
Mission: ingest these GitHub sources one by one.

- URL: https://github.com/owner/repo
  Assumed name:
  Why it matters:
  Priority: high / medium / low
  Decision question:
```

A plain list also works:

```md
https://github.com/owner/repo-a
https://github.com/owner/repo-b
```

## Procedure for Codex

1. Read `AGENTS.md`, `COMMUNICATION_PROTOCOL.md`, `CURRENT_STATE.md`, `INGESTION_PROTOCOL.md`, `SOURCE_INDEX.md`, `THEME_MAP.md`, `DECISIONS.md`, `PRODUCTION_CANDIDATES.md`, `RISK_REGISTER.md` and relevant skills in `.codex/skills/`.
2. Select the first unprocessed source only.
3. Read the primary source and capture evidence.
4. Decide whether clone/test is necessary.
5. If clone/test is necessary, use `repos/cloned/`, inspect scripts first and log commands.
6. Produce one decision-oriented source note in `sources/`.
7. Score the source and assign `KEEP`, `ADAPT`, `TEST`, `WATCH` or `REJECT`.
8. Create or update the relevant theme.
9. Update all transversal registries.
10. Update `CURRENT_STATE.md`, `NEXT_MISSION.md` and `HANDOFF.md` if state changes.
11. Run `.\scripts\check_workspace.ps1`.
12. Respond only with the compressed ingestion final format.

## Non-negotiable rule

Do not summarize a batch of repositories. Each repository must produce its own note, verdict, scoring, theme impact and registry updates.

## Current blockers

- None.

## Last completed source

- `github-dietrichgebert-ponytail`
- Verdict: ADAPT
- Theme: `agent-minimalism`
- Clone retained locally under ignored path `repos/cloned/ponytail`
