# HANDOFF

## Current state

`EGX_Ingestion` has been consolidated and is ready for the first real source ingestion.

No external source has been ingested. No external repository has been cloned. No dependencies have been installed.

Git has been initialized locally on branch `main`. The workspace has Git publication safeguards in `.gitignore`, `.gitattributes`, `SECURITY.md` and `GIT_PUBLISH_AUDIT.md`.

GitHub publication is pending because GitHub CLI (`gh`) is not installed or available in `PATH`.

Last local commit:

- Message: `Initial EGX_Ingestion workspace`
- Remote: not configured yet.
- GitHub visibility target: PRIVATE first.

## Files to read first

1. `AGENTS.md`
2. `CURRENT_STATE.md`
3. `NEXT_MISSION.md`
4. `INGESTION_PROTOCOL.md`
5. `SOURCE_INDEX.md`
6. `THEME_MAP.md`
7. `DECISIONS.md`
8. `PRODUCTION_CANDIDATES.md`
9. `RISK_REGISTER.md`
10. `.agents/skills/README.md`
11. `GIT_PUBLISH_AUDIT.md`

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

## Active skills

- `.agents/skills/source-ingestion`
- `.agents/skills/repo-lab-test`
- `.agents/skills/transversal-synthesis`

## Next action

Install GitHub CLI if publication is still needed:

```powershell
winget install --id GitHub.cli
```

Then restart the terminal, run browser authentication:

```powershell
gh auth login
```

After authentication, publish privately:

```powershell
gh repo create EGX_Ingestion --private --source=. --remote=origin --push
```

After the GitHub remote is configured and pushed, wait for the first GitHub URL or URL list, then follow `INGESTION_PROTOCOL.md`.

## Verification

Run:

```powershell
.\scripts\check_workspace.ps1
```

Expected result after consolidation: `Status: OK`.
