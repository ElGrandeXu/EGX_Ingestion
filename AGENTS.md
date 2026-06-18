# EGX_Ingestion Agent Instructions

## Workspace identity

This workspace is `EGX_Ingestion`.

Operational user name for this workspace: `Xü`; see `USER_CONTEXT.md`.

Purpose: research, ingest, test and transform technical or methodological sources into decision-ready knowledge. Future sources can include GitHub repositories, Reddit discussions, Hugging Face pages, official documentation, technical articles, architectures, agentic workflows, AI tools and development patterns.

This is not the production workspace. The future production workspace is `C:\Users\maxer\Desktop\EGX_Production`, and must not be created or modified from here without a later explicit mission.

Core split:

- `EGX_Ingestion` = research, ingestion, experimentation, testing, decision.
- `EGX_Production` = future production workspace built later from stabilized conclusions.

## Strict scope

- Keep all file creation, edits, deletion, moves, builds, tests and generated artifacts inside `C:\Users\maxer\Desktop\EGX_Ingestion`.
- Never create `EGX_Production` early.
- Never install dependencies outside this workspace.
- Never clone external repositories unless the current mission explicitly asks for source ingestion and the clone is justified.
- Clone only into `repos/cloned/`.
- Do not run build, demo, package install or test commands from an external repo until scripts and setup files have been read.
- Document practical experiments in `EXPERIMENT_LOG.md`; document external-repo commands in `logs/command-log.md`.
- Do not store secrets, tokens or API keys in notes.

## Fresh start

- Do not reuse assumptions from older workspaces.
- Do not reference older systems, project names or methods unless introduced by an ingested source in this workspace.
- Treat this workspace as Codex-native: durable instructions in `AGENTS.md`, readable workflows, Markdown notes, simple skills and explicit registers.

## Active instruction surfaces

- `AGENTS.md` is the durable repo instruction file.
- `COMMUNICATION_PROTOCOL.md` is the source of truth for user-visible communication.
- `.codex/skills/` is the primary Codex repo-scoped skill location.
- `.agents/skills/` is compatibility / historical mirror when needed.
- `skills/` is a human-readable documentary registry and reference mirror. If skill content diverges, `.codex/skills/` wins.
- `templates/` contains reusable templates for new notes and reports.
- `sources/`, `themes/`, root registries and logs are the durable knowledge base.

Do not add a new framework layer unless a later mission explicitly asks for it.

## Communication / token-saving

- Default mode: final-only.
- Do not send progress updates during work.
- Do not narrate reasoning or steps.
- Work silently until done.
- Speak only at final, or if blocked by auth/secret/destructive action/permission.
- Use `COMMUNICATION_PROTOCOL.md` as source of truth.
- Use `caveman-final-only` skill for all missions unless user explicitly asks for detailed narration.
- Reasoning depth remains high; visible output remains low.

## Organization by themes

- Do not organize knowledge primarily by source type such as `github`, `reddit` or `huggingface`.
- Source type is metadata in notes and registers.
- The main organization emerges by themes in `themes/`.
- Codex may create, rename, merge, split or link themes when sources justify it.
- Every theme change must be visible in `THEME_MAP.md` and in the affected theme folder.

## Source-by-source ingestion rule

Process exactly one source at a time.

For each source, finish the source note, scoring, verdict, theme update, transversal synthesis and handoff before moving to another source.

Every source note must clearly state:

- what to keep;
- what to reject;
- what to adapt;
- what to test;
- what influences `EGX_Production`;
- what is interesting but not priority;
- what is dangerous, fragile, too complex or noisy.

## Source-type handling

GitHub repository:

- Read the repo page, README, license, setup files and scripts relevant to the decision.
- Clone only if the clone or local inspection can change the verdict.
- If cloned, use `repos/cloned/`, read scripts before commands, and log commands.

Official documentation:

- Prefer the official page as primary source.
- Separate stable API or configuration facts from examples, marketing and optional practices.
- Capture version, date or currentness signals when available.

Technical article or blog post:

- Identify claims, evidence, assumptions and reproducible steps.
- Do not promote a pattern because it is persuasive; require practical value.

Reddit or discussion thread:

- Treat as anecdotal unless supported by concrete examples, links, repeated signals or reproducible failures.
- Capture disagreement and noise explicitly.

Hugging Face, model page or dataset page:

- Capture license, intended use, maturity, resource requirements and operational risk.
- Do not add a model or workflow to production candidates without practical constraints and a next test.

## Mandatory scoring

Each ingested source must receive:

- Verdict: `KEEP`, `ADAPT`, `TEST`, `WATCH` or `REJECT`
- Production potential: 1-5
- Practical value: 1-5
- Originality: 1-5
- Implementation complexity: 1-5
- Risk / noise: 1-5

Decision rules:

- Practical value beats novelty.
- Original but impractical sources do not become `EGX_Production` candidates.
- Complex sources are kept only when practical impact justifies the cost.
- A `TEST` verdict must create or propose a concrete experiment in `EXPERIMENT_LOG.md`.

## Mandatory pipeline after each source

After each ingested source, update at minimum:

- source note in `sources/`;
- relevant theme files in `themes/`;
- `SOURCE_INDEX.md`;
- `THEME_MAP.md`;
- `DECISIONS.md`;
- `PRODUCTION_CANDIDATES.md`;
- `RISK_REGISTER.md` if a risk exists or changes;
- `EXPERIMENT_LOG.md` if an experiment is run or proposed;
- `CURRENT_STATE.md`, `NEXT_MISSION.md` and `HANDOFF.md` when mission state or next action changes.

Never end an ingestion with only a neutral summary. The expected output is an exploitable decision.

## Done definition for an ingestion

A source is done only when:

- the note exists in `sources/` and includes verdict plus scores;
- clone/test decision is documented;
- all required registers are synchronized;
- theme impact is documented, even when no new theme is created;
- production impact is stated as candidate, indirect influence, no impact, test required or rejected;
- risks and experiments are either updated or explicitly marked not needed;
- next action is clear.

## Practical test rules

- Clone only when the source deserves local verification.
- Clone in `repos/cloned/`, never at the root.
- Archive or document any retained repo in `repos/archived/` or the relevant register.
- Before running any command from an external repo, read scripts and identify possible effects.
- Prefer diagnostic read-only commands before installs, builds, tests or demos.
- Document commands in `logs/command-log.md` and conclusions in `EXPERIMENT_LOG.md`.
- Do not run destructive or risky commands without a documented reason.

## Prohibited drift

- No dependency installed outside this workspace.
- No premature production workspace.
- No clone during initialization or audit unless explicitly required.
- No rigid platform taxonomy.
- No fragile pseudo-agent framework.
- No automatic promotion to `EGX_Production` without justification, score and next test.
- No source batching that hides per-source decisions.

## Minimal implementation ladder

Before adding files, scripts, folders, dependencies, abstractions or production candidates, apply `themes/agent-minimalism/minimal-implementation-ladder.md`: reuse existing doctrine/templates first, prefer the smallest reversible Markdown patch when automation is not needed, and keep tests, experiments, risk tracking and register synchronization intact.

## End-of-mission response

End each mission with the shortest format allowed by `COMMUNICATION_PROTOCOL.md`.
