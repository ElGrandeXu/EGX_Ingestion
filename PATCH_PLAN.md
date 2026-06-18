# PATCH_PLAN

Date: 2026-06-18

| Probleme identifie | Fichier concerne | Correction proposee | Raison | Risque | Statut |
|---|---|---|---|---|---|
| `AGENTS.md` est bon mais manque de consignes operationnelles par type de source et definition stricte de fin d'ingestion | `AGENTS.md` | Ajouter workflow par type, definition de done, role skills/templates, handoff | Eviter les resumes neutres et les oublis de registres | Faible, instructions plus precises | apply |
| `.agents/skills/` est actif mais contient des skills abreges | `.agents/skills/*/SKILL.md` | Rendre les skills actifs autosuffisants et plus prescriptifs | Codex decouvre les skills repo dans `.agents/skills/` | Faible | apply |
| `skills/` et `.agents/skills/` peuvent diverger | `skills/README.md`, `.agents/skills/README.md` | Documenter que `.agents/skills/` est actif et que `skills/` est documentaire | Eviter une mauvaise source de verite | Faible | apply |
| Templates trop courts pour une ingestion GitHub robuste | `templates/*.md`, `sources/_template_source_note.md`, `experiments/_template_experiment.md` | Ajouter champs obligatoires, decisions, scores, risques, liens et prochaines actions | Forcer une note decisionnelle exploitable | Moyen si trop lourd, garder format simple | apply |
| Protocole d'ingestion incomplet sur handoff et clone/test | `INGESTION_PROTOCOL.md`, `RUNBOOK.md` | Ajouter gate de clone/test, ordre exact des mises a jour, handoff | Eviter les oublis source par source | Faible | apply |
| `NEXT_MISSION.md` trop general pour une liste d'URLs GitHub | `NEXT_MISSION.md` | Ajouter prompt pret a l'emploi et regle de traitement sequentiel | Permettre la prochaine mission GitHub directement | Faible | apply |
| Registres minimaux mais maintenables | `SOURCE_INDEX.md`, `DECISIONS.md`, `PRODUCTION_CANDIDATES.md`, `RISK_REGISTER.md`, `EXPERIMENT_LOG.md` | Ajouter colonnes/statuts sans refonte lourde | Mieux preparer ingestion et production future | Faible | apply |
| Check PowerShell trop permissif | `scripts/check_workspace.ps1` | Verifier non-vide, frontmatter skills, templates non vides, affichage clair | Eviter faux OK | Faible, script lecture seule | apply |
| Etat et handoff obsoletes apres consolidation | `CURRENT_STATE.md`, `HANDOFF.md` | Mettre a jour l'etat reel, limites et prochaine action | Reprise fiable | Faible | apply |
| Creation d'une configuration Codex locale | `.codex/config.toml` | Ne pas creer maintenant | Le workspace n'a pas besoin d'une couche config supplementaire pour l'ingestion | Evite complexite | skip |
| Suppression de `skills/` | `skills/` | Ne pas supprimer | Pas de raison forte; garder comme registre documentaire | Evite perte historique | skip |
| Clone d'un repo pour tester le protocole | `repos/cloned/` | Ne pas cloner | Interdit par la mission | Aucun | skip |
| Alignement automatique parfait des deux copies de skills | `skills/*/SKILL.md` et `.agents/skills/*/SKILL.md` | Garder `.agents/skills/` canonique et documenter `skills/` comme miroir documentaire | Eviter maintenance complexe | Divergence possible si futur edit manuel | defer |

## Execution note

All rows marked `apply` were applied during the 2026-06-18 consolidation. Rows marked `skip` were intentionally not applied. The `defer` row remains a known maintenance risk tracked in `RISK_REGISTER.md`.
