# HANDOFF

## Current state

`EGX_Ingestion` has been consolidated, published and updated with a final-only token-saving communication doctrine. The first real source ingestion is complete.

Ingested source:

- ID: `github-dietrichgebert-ponytail`
- URL: https://github.com/DietrichGebert/ponytail
- Verdict: ADAPT
- Primary theme: `agent-minimalism`
- Source note: `sources/github-dietrichgebert-ponytail.md`
- Clone retained locally: `repos/cloned/ponytail` (ignored by git)
- Dependencies installed: none

Git has been initialized locally on branch `main`. The workspace has Git publication safeguards in `.gitignore`, `.gitattributes`, `SECURITY.md` and `GIT_PUBLISH_AUDIT.md`.

GitHub publication is complete. The private repository is `ElGrandeXu/EGX_Ingestion` at `https://github.com/ElGrandeXu/EGX_Ingestion`.

Previous published commit before Ponytail ingestion:

- Message: `Initial EGX_Ingestion workspace`
- Commit: `d074df0`
- Remote: `origin` -> `https://github.com/ElGrandeXu/EGX_Ingestion.git`.
- GitHub visibility: `PRIVATE`.

GitHub CLI note:

- Installed executable: `C:\Program Files\GitHub CLI\gh.exe`.
- The short `gh` command was not available in the current PowerShell `PATH` during publication.
- GitHub authentication succeeded for `ElGrandeXu` with HTTPS.

## Files to read first

1. `AGENTS.md`
2. `CURRENT_STATE.md`
3. `COMMUNICATION_PROTOCOL.md`
4. `NEXT_MISSION.md`
5. `INGESTION_PROTOCOL.md`
6. `SOURCE_INDEX.md`
7. `THEME_MAP.md`
8. `DECISIONS.md`
9. `PRODUCTION_CANDIDATES.md`
10. `RISK_REGISTER.md`
11. `.codex/skills/README.md`
12. `GIT_PUBLISH_AUDIT.md`

## Essential rules

- Stay inside `C:\Users\maxer\Desktop\EGX_Ingestion`.
- Treat sources one by one.
- Produce decision-oriented source notes.
- Score every ingested source.
- Document clone/test decisions.
- Update transversal registries after every source.
- Do not create `EGX_Production`.
- Do not commit future contents of `repos/cloned/`, `repos/archived/` or `experiments/runs/` except their `.gitkeep` files.
- Keep `logs/*.md` versioned as controlled memory, but do not commit raw `*.log` files.
- Use final-only communication by default. No progress narration.

## Active skills

- `.codex/skills/caveman-final-only`
- `.codex/skills/source-ingestion`
- `.codex/skills/repo-lab-test`
- `.codex/skills/transversal-synthesis`

Compatibility mirrors remain under `.agents/skills/`.

## Current theme state

- Active theme: `agent-minimalism`, maturity 2.
- Production candidate: `PC-0001` adapted minimal implementation ladder, status `test-required`.
- Experiments: `EXP-0001` done; `EXP-0002` proposed.

## Next action

Either run `EXP-0002` or wait for the next single source URL. Do not clone unless the source note justifies local inspection, and clone only into `repos/cloned/`. Final user reply must be compressed.

## Verification

Run:

```powershell
.\scripts\check_workspace.ps1
```

Expected result after consolidation: `Status: OK`.
