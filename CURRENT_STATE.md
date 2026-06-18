# CURRENT_STATE

Date: 2026-06-18

## Workspace state

Workspace consolidated from initial scaffolding into a usable Codex-native ingestion workspace. A final-only token-saving communication doctrine is installed. The first real source ingestion is complete: `github-dietrichgebert-ponytail`.

An external repository was cloned inside the allowed ignored path: `repos/cloned/ponytail`. No dependency was installed.

Git has been initialized locally on branch `main`. GitHub publication is complete: the private GitHub repository `ElGrandeXu/EGX_Ingestion` exists and `origin/main` tracks it.

## Consolidation completed

- `AGENTS.md` now defines source-by-source ingestion, source-type handling, done criteria and strict scope.
- `.codex/skills/` is the primary Codex repo-scoped skill location.
- `.agents/skills/` is retained as compatibility mirror.
- `skills/` is a documentary mirror and registry.
- `COMMUNICATION_PROTOCOL.md` and `TOKEN_SAVING_DOCTRINE.md` define final-only communication.
- Templates now force metadata, verdicts, scores, clone/test decision, production impact, risks and next actions.
- Root registries now include status, evidence and verification fields.
- `INGESTION_PROTOCOL.md` and `RUNBOOK.md` now describe GitHub ingestion and handoff more explicitly.
- `scripts/check_workspace.ps1` is expected to verify non-empty files, templates and skill frontmatter.

## Doctrine active

- One source at a time.
- Decision notes, not neutral summaries.
- Practical value beats novelty.
- Themes emerge progressively.
- Scoring is mandatory for every ingested source.
- Transversal synthesis is mandatory after every source, including rejected sources.
- `EGX_Production` remains uncreated and untouched.
- Final-only communication is mandatory by default; synthesis goes into files, not chat narration.

## Current content status

- Sources ingested: 1 (`github-dietrichgebert-ponytail`).
- Active themes: `agent-minimalism`.
- Production candidates: `PC-0001` adapted minimal implementation ladder, status `test-required`.
- Experiments launched: `EXP-0001` done; `EXP-0002` proposed.
- Known workspace risks: ingestion/production confusion, skill mirror divergence, communication compression, plugin sprawl, minimalism/neglect confusion, always-on rule cost and benchmark hype.
- Git local repository: initialized on `main`.
- GitHub remote: `origin` -> `https://github.com/ElGrandeXu/EGX_Ingestion.git`.
- GitHub visibility: `PRIVATE`.
- Active Git protections: `.gitignore`, `.gitattributes`, `SECURITY.md` and `GIT_PUBLISH_AUDIT.md`.

## Git publication status

- `git`: installed.
- `gh`: installed at `C:\Program Files\GitHub CLI\gh.exe`; the short `gh` command is not available in the current PowerShell `PATH`.
- GitHub authentication: successful for `ElGrandeXu` using HTTPS.
- GitHub repository: `https://github.com/ElGrandeXu/EGX_Ingestion`.
- Local initial commit pushed: `d074df0 Initial EGX_Ingestion workspace`.
- Documentation update pending or completed in a follow-up commit named `Document GitHub publication`.

## Next step

Either ingest the next single source or run `EXP-0002`, a bounded comparison of normal implementation vs adapted minimalism checklist before promoting `PC-0001`.
