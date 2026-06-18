# QUALITY_AUDIT

Date: 2026-06-18

## References consultees

- Codex overview: https://developers.openai.com/codex
- AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- Skills: https://developers.openai.com/codex/skills
- Best practices: https://developers.openai.com/codex/learn/best-practices
- Config basics: https://developers.openai.com/codex/config-basic
- Config reference: https://developers.openai.com/codex/config-reference

Points utiles pour ce workspace:

- `AGENTS.md` est un bon support durable pour les regles de repo, contraintes, commandes et definition de "done".
- Codex decouvre les skills de repo dans `.agents/skills/`; chaque skill doit etre un dossier avec `SKILL.md` et un frontmatter contenant `name` et `description`.
- Les descriptions de skills doivent etre assez explicites pour le declenchement implicite.
- Un `AGENTS.md` court et actionnable vaut mieux qu'un long fichier vague.

## Resume brutal de l'etat initial

Solide:

- La separation `EGX_Ingestion` / `EGX_Production` est explicite.
- Les registres racine existent et couvrent les bonnes categories: sources, themes, decisions, candidats production, risques, experiences.
- Le protocole impose deja une logique source par source.
- Les trois skills utiles existent: ingestion source, test repo, synthese transversale.
- Le check PowerShell initial n'a pas d'effet de bord visible.

Superficiel:

- Plusieurs fichiers sont plus proches du scaffolding que d'outils de travail, surtout les templates et quelques registres.
- Le script `check_workspace.ps1` valide surtout la presence, pas la qualite minimale.
- Les skills actives dans `.agents/skills/` sont des versions reduites qui renvoient vers `skills/`, ce qui affaiblit le declenchement et l'autonomie.

Manquant:

- Pas de check explicite des fichiers non vides.
- Pas de validation minimale du frontmatter YAML des skills.
- Pas de controle des templates non vides.
- Pas de workflow clair pour une liste de plusieurs URLs GitHub avec traitement d'une seule source a la fois.
- Pas de section de mini-simulation ou de check workflow dans l'audit initial.

Incoherent:

- `skills/` et `.agents/skills/` coexistent avec des contenus differents.
- La documentation dit que `.agents/skills/` est actif, mais les versions completes sont dans `skills/`.
- Les templates `templates/` et les templates locaux dans `sources/` / `experiments/` ne sont pas totalement alignes.

Risque pour les futures ingestions:

- Codex pourrait activer un skill trop court et produire un resume neutre au lieu d'une decision.
- Une ingestion GitHub pourrait cloner ou tester sans justification assez claire.
- Les registres pourraient diverger parce que le protocole ne force pas assez le passage note source -> theme -> synthese -> handoff.
- Le check pourrait afficher OK alors qu'un template ou un skill serait vide.

## Audit AGENTS.md

Lecture par Codex:

- Oui, le fichier est a la racine du workspace. Les docs officielles indiquent que Codex lit les fichiers `AGENTS.md` de projet avant le travail, avec les fichiers proches du cwd qui priment.

Longueur:

- 85 lignes, environ 5 Ko. C'est acceptable et sous le seuil par defaut mentionne par la documentation, mais certaines regles peuvent etre condensees ou rendues plus operationnelles.

Actionnable:

- Globalement oui. Les contraintes de scope, scoring, pipeline et fin de mission sont nettes.
- A renforcer: mode de traitement par type de source, ordre exact des fichiers a mettre a jour, definition d'une ingestion terminee.

Mises a jour apres chaque source:

- Oui, la liste minimale est presente.
- A renforcer: `CURRENT_STATE.md`, `NEXT_MISSION.md` et `HANDOFF.md` quand la mission change ou qu'une source est traitee.

Anti-derive:

- Les interdictions principales sont bonnes.
- A renforcer: pas de clone sans decision documentee, pas de commande de repo externe sans lecture des scripts, pas de promotion production sans preuve.

Distinction ingestion / production:

- Bonne et explicite.

Regles de fin de mission:

- Presentes et compatibles avec la demande utilisateur.

GitHub, Reddit, Hugging Face, docs, articles:

- Les types sont cites, mais il manque une consigne operationnelle par type. GitHub est mieux couvert que les autres.

## Audit skills

Etat initial:

- Les six `SKILL.md` existent: trois dans `skills/` et trois dans `.agents/skills/`.
- Tous les `SKILL.md` contiennent un frontmatter YAML avec `name` et `description`.
- Les descriptions sont correctes pour un declenchement implicite.
- Chaque skill vise un seul job.

Probleme:

- `.agents/skills/` est l'emplacement actif Codex pour les skills partages du workspace.
- Les versions actives sont plus courtes que les versions de `skills/` et deleguent vers elles.
- Comme le declenchement et la lecture active passent par `.agents/skills/`, les versions actives doivent etre autosuffisantes.

Decision:

- `.agents/skills/` devient la version active et canonique pour Codex.
- `skills/` devient un registre documentaire lisible qui peut garder un miroir de reference, mais ne doit pas etre considere comme source active.
- Ne rien supprimer pendant cette consolidation. La divergence doit etre reduite par documentation et, si possible, par alignement du contenu.

## Audit templates

Constat:

- `source-note-template.md` est le meilleur template initial, mais il manque auteur/org, licence, maturite, decision de clone/test, liens transversaux et prochaines actions.
- `theme-note-template.md` est exploitable mais trop court pour maintenir un theme actif.
- `experiment-template.md` ne force pas assez la lecture des scripts ni le journal de commandes.
- `production-candidate-template.md` est utile mais manque les conditions de rejet/retrogradation.
- `handoff-template.md` est trop court pour une reprise fiable.
- `ingestion-report-template.md` ressemble a un resume, pas encore a un rapport decisionnel.

Exigences a imposer:

- Source, URL, type, theme principal, themes secondaires.
- Resume court et utile.
- Keep / reject / adapt / test.
- Verdict et scores 1-5.
- Impact `EGX_Production`.
- Risques, liens transversaux, prochaines actions.

## Audit protocole d'ingestion

Solide:

- Le protocole couvre identification, lecture, decision clone/test, note source, theme, scoring, verdict et synthese.

Faible:

- Le clone/test n'exige pas encore une question de decision precise.
- Le protocole ne force pas assez les liens vers `logs/command-log.md`.
- Le handoff n'est pas une etape obligatoire.
- Le traitement d'une liste d'URLs GitHub doit etre plus explicite: prendre la premiere source, finir toutes les mises a jour, puis seulement passer a la suivante.

## Audit logs / index

`SOURCE_INDEX.md`:

- Tableau utilisable.
- A renforcer avec statut de traitement et decision de clone/test.

`DECISIONS.md`:

- Actionnable mais minimal.
- A renforcer avec type de decision et prochaine verification.

`PRODUCTION_CANDIDATES.md`:

- Bonne base.
- A renforcer avec condition d'entree et condition de sortie.

`EXPERIMENT_LOG.md`:

- Bonne base pour tracer les commandes.
- A renforcer avec lien vers `logs/command-log.md` et statut d'experience.

`RISK_REGISTER.md`:

- Couvre deja pollution workspace, dependances lourdes, hype, securite, complexite.
- A renforcer avec triggers et statuts simples.

## Audit script

Etat initial:

- Verifie les fichiers essentiels, dossiers, templates et skills.
- Affiche clairement les sections.
- Pas d'effet de bord constate.

Manques:

- Ne verifie pas que les fichiers essentiels sont non vides.
- Ne verifie pas que les templates sont non vides.
- Ne verifie pas que les skills contiennent un frontmatter avec `name` et `description`.
- Ne signale pas la divergence potentielle entre `skills/` et `.agents/skills/`.

## Mini-simulation FAKE_SOURCE_DO_NOT_KEEP

Etat initial:

- En suivant `INGESTION_PROTOCOL.md`, on sait qu'il faudrait creer une note source, scorer, mettre a jour `SOURCE_INDEX.md`, `THEME_MAP.md`, `DECISIONS.md`, `PRODUCTION_CANDIDATES.md`, `RISK_REGISTER.md` si besoin, `EXPERIMENT_LOG.md` si besoin et le theme.
- Le workflow est comprehensible mais pas encore assez contraignant pour garantir le handoff et la decision clone/test.

Etat apres consolidation:

- La simulation mentale avec `FAKE_SOURCE_DO_NOT_KEEP` indique maintenant un chemin clair sans creer de fausse source:
  1. selectionner une seule source;
  2. attribuer un ID temporaire seulement dans le raisonnement;
  3. lire la source primaire;
  4. documenter la decision de clone/test;
  5. produire une note source dans `sources/` si c'etait une vraie ingestion;
  6. scorer et choisir `KEEP`, `ADAPT`, `TEST`, `WATCH` ou `REJECT`;
  7. mettre a jour theme, `SOURCE_INDEX.md`, `THEME_MAP.md`, `DECISIONS.md`, `PRODUCTION_CANDIDATES.md`, `RISK_REGISTER.md` et `EXPERIMENT_LOG.md` si necessaire;
  8. mettre a jour `CURRENT_STATE.md`, `NEXT_MISSION.md` et `HANDOFF.md` si l'etat change.
- Le protocole indique maintenant explicitement de ne pas laisser de fausse source dans les registres.
- Aucune entree `FAKE_SOURCE_DO_NOT_KEEP` n'a ete ajoutee a `SOURCE_INDEX.md`.

## Consolidation appliquee

- `AGENTS.md` renforce: source-by-source, types de sources, definition de done, interdictions et surfaces actives.
- `.agents/skills/` renforce: les trois skills actives sont autosuffisantes avec frontmatter valide.
- `skills/` clarifie: miroir documentaire, non source active si divergence.
- Templates renforces: metadata, evidence, verdict, scores, clone/test, risques, impact production, liens et prochaines actions.
- Registres renforces: statuts, preuves, prochaine verification, risques et conditions de migration.
- `INGESTION_PROTOCOL.md` renforce: gate clone/test, synthese transversale, handoff et check final par source.
- `NEXT_MISSION.md` renforce: pret pour une liste d'URLs GitHub traitee source par source.
- `scripts/check_workspace.ps1` renforce: presence, non-vide, templates, skills et frontmatter.

## Limites restantes

- Aucun vrai repo GitHub n'a encore ete ingere, donc la robustesse sera confirmee lors de la premiere ingestion reelle.
- Le miroir `skills/` peut encore diverger dans le futur si les edits ne commencent pas par `.agents/skills/`.
- Les themes sont volontairement vides tant qu'aucune source n'a ete ingeree.
- Le workspace n'est pas un depot Git initialise, donc l'audit ne peut pas s'appuyer sur un diff Git local.

## Check final

- Check initial execute: `.\scripts\check_workspace.ps1`
- Resultat initial: OK, mais check trop permissif.
- Check intermediaire apres patch execute: `.\scripts\check_workspace.ps1`
- Resultat intermediaire: OK. Le script valide maintenant les fichiers non vides, templates non vides et frontmatter des skills.
- Check final execute: `.\scripts\check_workspace.ps1`
- Resultat final: OK. Le script confirme les fichiers racine non vides, dossiers requis, templates non vides, fichiers de theme template, skills actives et miroir documentaire, frontmatter `name`/`description`, et decision d'emplacement des skills.
