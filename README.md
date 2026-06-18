# EGX_Ingestion

`EGX_Ingestion` is a Codex-native workspace for research, source ingestion, practical experimentation and decision-making.

It turns technical and methodological sources into knowledge that can later inform `EGX_Production`. It is not the production workspace.

This workspace is not:

- a production codebase;
- a bookmark dump;
- a GitHub mirror;
- a platform-based taxonomy;
- a place to install or test outside scope;
- a framework for agents.

## Start an ingestion

Provide one or more URLs in the prompt, or add them to `inbox/sources_to_ingest.md`.

Recommended format:

```md
- URL: https://github.com/owner/repo
  Assumed name:
  Why it matters:
  Priority: high / medium / low
  Decision question:
```

A plain list of URLs is enough. Codex must process them one by one.

## Required workflow

For each source:

1. Follow `INGESTION_PROTOCOL.md`.
2. Produce one source note in `sources/`.
3. Assign verdict and scores.
4. Document clone/test decision.
5. Update the relevant theme in `themes/`.
6. Update transversal registries.
7. Update handoff files when state changes.

Do not move to the next source until the current source is complete.

## Main files

- Durable instructions: `AGENTS.md`
- Procedure: `INGESTION_PROTOCOL.md`, `RUNBOOK.md`
- Communication: `COMMUNICATION_PROTOCOL.md`, `TOKEN_SAVING_DOCTRINE.md`
- Source notes: `sources/`
- Themes: `themes/`
- Source registry: `SOURCE_INDEX.md`
- Theme map: `THEME_MAP.md`
- Decisions: `DECISIONS.md`
- Production candidates: `PRODUCTION_CANDIDATES.md`
- Risks: `RISK_REGISTER.md`
- Experiments: `EXPERIMENT_LOG.md`, `experiments/`
- Commands: `logs/command-log.md`
- Primary Codex skills: `.codex/skills/`
- Compatibility skill mirror: `.agents/skills/`
- Documentary skill mirror: `skills/`

## Future EGX_Production

Migration to `EGX_Production` is not automatic. It must be based on:

- documented production candidates;
- decisions;
- risks;
- experiments;
- practical-value evidence.

Do not create `EGX_Production` from this workspace unless a later explicit mission asks for it.
