# github-dietrichgebert-ponytail

## Identity

* Source: Ponytail
* URL: https://github.com/DietrichGebert/ponytail
* Type: GitHub repository
* Owner: DietrichGebert
* License: MIT
* Local clone: `repos/cloned/ponytail`
* Ingestion date: 2026-06-18

## What it is

Ponytail is an agent-portable rule, skill and plugin distribution for forcing smaller, less speculative code changes. It packages the same core method for Codex, Claude Code, OpenCode, Gemini, Copilot, Cursor, Windsurf, Cline, Kiro, OpenClaw and pi-style agents.

The repository is not a production application. It is a methodology plus adapter set: rules, skills, hooks, commands, tests, examples and benchmarks.

Repository metadata from GitHub API on 2026-06-18:

* Description: "Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote."
* Primary language: JavaScript
* Topics include `agent-skills`, `ai-agents`, `claude-code-plugin`, `cursor-rules`, `developer-tools`, `prompt-engineering`, `yagni`
* Public repository, default branch `main`
* Latest inspected commit: `8d5037d docs(readme): add the agentic benchmark chart (#160)`

## Core mechanism

The core method is a decision ladder applied before writing code:

1. Does this need to exist at all?
2. Does the standard library already do it?
3. Does a native platform feature cover it?
4. Does an already-installed dependency solve it?
5. Can it be one line?
6. Only then write the minimum working code.

The important distinction is "lazy, not negligent": Ponytail explicitly excludes trust-boundary validation, data-loss prevention, security, accessibility, hardware calibration and explicit user requirements from code-cutting. It also requires one small runnable check for non-trivial logic.

The repo reinforces the method through:

* `AGENTS.md`: compact always-on instruction text.
* `skills/ponytail/SKILL.md`: longer runtime skill with triggers and levels.
* `skills/ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-help`.
* `hooks/`: activation, mode tracking, instruction building and statusline helpers.
* `commands/`: command definitions for compatible hosts.
* `.codex-plugin/plugin.json`: Codex plugin metadata pointing to `skills/`.
* Multiple agent-specific adapters: `.claude-plugin`, `.github/plugin`, `.cursor`, `.windsurf`, `.clinerules`, `.kiro`, `.opencode`, `.openclaw`, `gemini-extension.json`, `pi-extension`.
* `benchmarks/`: single-shot and agentic benchmark harnesses and results.
* `tests/`: Node test suite for behavior, commands, hooks, plugin adapters and benchmark graders.

## Codex relevance

Direct Codex relevance is real but should not be installed into this workspace:

* `.codex-plugin/plugin.json` declares Ponytail as a Codex plugin with instructions and lifecycle hooks.
* `skills/` contains Codex-compatible `SKILL.md` files.
* `hooks/hooks.json` and Node hook scripts can inject rules and track modes.
* README states Codex plugin installation through marketplace and plugin UI.
* Codex extension can also read `AGENTS.md` as instruction-tier behavior.

For `EGX_Ingestion`, the useful Codex transfer is methodological, not mechanical. Installing Ponytail would create rule-stack drift against the current final-only Caveman doctrine and would add always-on context/hook behavior before this workspace has tested whether it needs it.

## What to keep

* The decision ladder: YAGNI -> stdlib -> native -> existing dependency -> one-liner -> minimum implementation.
* The phrase-level distinction between minimalism and negligence.
* The explicit non-negotiables: validation, data-loss prevention, security, accessibility, physical calibration and explicit user requirements.
* The "one runnable check" rule for non-trivial logic.
* The review/audit/debt split: diff review, repo audit and explicit tracking of accepted shortcuts.
* The adapter-thinness pattern: keep core instructions centralized, generate or verify copies.
* The benchmark humility: corrected benchmark claims after critique, explicit contaminated-run disclosure and reproducibility notes.

## What to reject

* Installing the Ponytail plugin in `EGX_Ingestion`.
* Adding Ponytail as an always-on workspace rule.
* Copying its adapter tree or hook system into this workspace.
* Treating line count as the only objective.
* Importing its humorous/persona layer as doctrine.
* Accepting headline benchmark numbers without context: older single-shot numbers are explicitly described as inflated by a chatty baseline.

## What to adapt

* Create a local `agent-minimalism` theme to track code-economy discipline separately from token-saving communication discipline.
* Adapt the ladder as a future EGX_Production candidate rule, but only after testing it on real implementation tasks.
* Add a future experiment comparing normal Codex behavior, Caveman final-only and an adapted minimal-implementation checklist on one bounded coding task.
* Use `ponytail:`-style debt markers as an inspiration, not a literal namespace, for intentional shortcuts that name ceiling plus upgrade trigger.
* Reuse the "core rule + thin adapters + drift tests" design pattern if EGX_Production later needs portable agent instructions.

## What to test further

* Whether adding an explicit implementation-minimalism checklist reduces unnecessary files/dependencies in a real EGX_Production task without hiding required validation.
* Whether final-only communication plus implementation minimalism conflict: shorter visible output does not guarantee smaller or safer code.
* Whether a debt-ledger convention is useful enough to maintain.
* Whether a review-only `agent-minimalism` audit is safer than always-on rule injection.

## Practical test

Commands run locally inside `repos/cloned/ponytail`:

* `git status --short` -> clean clone.
* `git log --oneline -5` -> latest inspected commit `8d5037d`.
* `Get-ChildItem -Force` and `Get-ChildItem -Recurse -Depth 2 -Force` -> confirmed multi-agent adapter structure, benchmarks, docs, hooks, commands, skills and tests.
* `npm test` -> failed with 50 passing tests and 1 failing test. The failing check is `csv: correct pandas one-liner passes`; local Python lacks pandas: `ModuleNotFoundError: No module named 'pandas'`.
* `python --version` -> Python 3.12.10.
* `python -c "import pandas; print(pandas.__version__)"` -> failed, pandas absent.
* `node --version` -> v24.13.0.
* `npm --version` -> 11.11.1.
* `node scripts\check-rule-copies.js` -> pass, rule copies match `AGENTS.md`; 8 invariants present.
* `npm test --prefix pi-extension` -> pass, 11 tests.

No dependency install was run. The failed root test is environmental, not enough to reject the repo, because GitHub Actions explicitly installs pandas before `npm test`.

## Theme impact

Primary theme: `agent-minimalism`.

Secondary links:

* `token-saving / caveman-final-only`: related but distinct. Caveman governs user-visible communication; Ponytail governs implementation size and code choices.
* Future `agent-portability`: Ponytail is strong evidence that portable agent instructions need drift checks across host-specific copies.
* Future `benchmark-discipline`: Ponytail provides a useful example of correcting inflated claims with a better agentic benchmark.

## Production impact

Label: candidate production element.

Candidate is not Ponytail as a plugin. Candidate is an adapted minimal implementation ladder for future `EGX_Production` engineering work:

* start from YAGNI;
* prefer standard library and native platform features;
* reuse installed dependencies before adding new ones;
* keep explicit safety carve-outs;
* leave one runnable check for non-trivial logic;
* mark intentional shortcuts with ceiling and upgrade trigger.

This should enter `EGX_Production` only after a bounded experiment.

## Risks

| Risk | Severity 1-5 | Mitigation | Register update needed |
|---|---:|---|---|
| Installing too many agent plugins before the workspace has stable needs | 4 | Treat Ponytail as source evidence, not active tooling | yes |
| Confusing minimalism with negligence | 4 | Preserve safety carve-outs and one-check rule | yes |
| Over-injecting always-on rules increases context cost and instruction conflicts | 3 | Prefer review/checklist experiment before always-on mode | yes |
| Benchmark hype from LOC-only metrics | 3 | Use agentic tests and preserve caveats | yes |
| Plugin hooks writing to user config or runtime state if installed casually | 3 | Do not install globally or locally in this workspace | yes |

## Verdict

Verdict principal: ADAPT

Scores:

* Production potential: 4
* Practical value: 5
* Originality: 3
* Implementation complexity: 2
* Risk / noise: 3

Rationale:

* Production potential is high for the adapted method, not for the full plugin.
* Practical value is strong because the ladder maps directly to avoiding dependency and abstraction bloat.
* Originality is moderate: YAGNI and stdlib-first are old, but packaging across agents plus safety carve-outs and benchmarks is useful.
* Implementation complexity is low if adapted as a checklist/review skill; higher if copied as hooks/plugins, which is rejected.
* Risk/noise is medium due to hype framing, always-on context cost and temptation to underbuild.

## Final decision

Adapt the method, not the plugin. Keep Ponytail as a source for `agent-minimalism`, create a future experiment, and reject installation or always-on rule injection in `EGX_Ingestion`.

