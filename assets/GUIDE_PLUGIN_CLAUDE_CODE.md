# Guide de développement d’un plugin Claude Code

> Note contexte repository : ce document est un guide générique.
> Le repository `fiscal-fr` courant contient le plugin Claude et sa configuration MCP, mais pas le code source d'un `mcp-server/` local.

## 1. Objectif

Ce document sert de guide pratique pour concevoir, développer, tester et faire évoluer un plugin Claude Code, avec une orientation produit et ingénierie.

Il couvre :
- la structure d’un plugin ;
- les composants disponibles ;
- le workflow de développement ;
- les bonnes pratiques ;
- un squelette recommandé pour un plugin métier ;
- une bibliographie officielle pour aller plus loin.

---

## 2. Ce qu’est un plugin Claude Code

Un plugin Claude Code est un répertoire versionnable qui regroupe une ou plusieurs extensions de comportement pour Claude Code.

Un plugin peut embarquer :
- des **skills** ;
- des **subagents** ;
- des **hooks** ;
- des **serveurs MCP** ;
- éventuellement des **LSP servers** ;
- des **settings** par défaut ;
- des exécutables utilitaires.

Le plugin est identifié par un manifeste :

```text
.claude-plugin/plugin.json
```

Le nom du plugin sert notamment de **namespace** pour les skills.

Exemple :

```text
/fiscal-fr:assistant-fiscal
```

---

## 3. Quand utiliser un plugin plutôt que `.claude/`

Utiliser un plugin quand :
- le comportement doit être partagé ;
- le travail doit être versionné ;
- le même ensemble d’outils doit être réutilisé dans plusieurs projets ;
- on veut distribuer une extension cohérente ;
- on veut éviter les conflits de noms grâce au namespace plugin.

Utiliser `.claude/` quand :
- on expérimente ;
- le besoin est strictement local à un projet ;
- on ne veut pas encore packager proprement.

Approche recommandée :
1. prototyper vite en `.claude/` si besoin ;
2. stabiliser ;
3. convertir en plugin.

---

## 4. Structure minimale d’un plugin

```text
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── my-skill/
│       └── SKILL.md
├── agents/
│   └── specialist.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── .lsp.json
├── settings.json
└── bin/
```

### Règle importante

Seul `plugin.json` doit être dans `.claude-plugin/`.

Les dossiers suivants doivent rester à la racine du plugin :
- `skills/`
- `agents/`
- `hooks/`
- `bin/`
- `.mcp.json`
- `.lsp.json`
- `settings.json`

---

## 5. Manifeste du plugin

### Exemple minimal

```json
{
  "name": "fiscal-fr",
  "description": "Assistant fiscal MVP pour la préparation de la déclaration française",
  "version": "0.1.0",
  "author": {
    "name": "Fabrice"
  }
}
```

### Champs utiles

- `name` : identifiant du plugin et namespace ;
- `description` : description visible dans l’écosystème plugin ;
- `version` : version sémantique ;
- `author` : attribution ;
- éventuellement `homepage`, `repository`, `license`.

### Bonnes pratiques

- utiliser un nom simple en `kebab-case` ;
- versionner proprement (`MAJOR.MINOR.PATCH`) ;
- garder une description produit claire et courte.

---

## 6. Skills

Les skills servent à étendre le comportement de Claude.

### Structure

```text
skills/
└── assistant-fiscal/
    └── SKILL.md
```

### Exemple

```md
---
name: assistant-fiscal
description: Lance un assistant fiscal français pour qualification, justificatifs ou préparation de pré-déclaration.
disable-model-invocation: true
---

Tu es un assistant fiscal français de préparation de déclaration.
```

### Points clés

- le fichier est toujours `SKILL.md` ;
- le frontmatter YAML contient au minimum une `description` utile ;
- le nom du dossier devient le nom du skill ;
- dans un plugin, le skill est namespacé.

### Invocation

```text
/fiscal-fr:assistant-fiscal
```

### Arguments

Le placeholder `$ARGUMENTS` permet de récupérer le texte passé après le skill.

Exemple :

```text
/fiscal-fr:assistant-fiscal qualification
```

### Bonnes pratiques skills

- un skill = une intention claire ;
- éviter les prompts géants et fourre-tout ;
- documenter explicitement les limites ;
- distinguer orchestration, spécialisation et logique métier ;
- utiliser les skills pour le comportement, pas comme substitut total à un moteur de règles.

---

## 7. Subagents

Les subagents permettent de spécialiser des tâches.

### Cas d’usage typiques

- qualification ;
- audit ;
- synthèse ;
- revue ;
- contrôle ;
- transformation métier.

### Structure

```text
agents/
└── tax-qualifier.md
```

### Exemple minimal

```md
---
name: tax-qualifier
description: Qualifie une situation fiscale française simple.
tools: "*"
model: sonnet
---

Tu es un spécialiste de la qualification fiscale.
```

### Bonnes pratiques subagents

- spécialiser fortement chaque agent ;
- limiter son rôle ;
- imposer un format de sortie stable ;
- éviter qu’un subagent “fasse tout” ;
- utiliser les subagents comme couche analytique, pas comme vérité métier si un MCP existe.

---

## 8. MCP

MCP (Model Context Protocol) permet de connecter Claude Code à des outils externes et des serveurs locaux ou distants.

Pour un plugin métier, MCP est la meilleure brique pour exposer une logique déterministe.

### Cas d’usage

- appeler une base métier ;
- exécuter des contrôles ;
- exposer des outils structurés ;
- encapsuler des règles ;
- interroger un corpus documentaire normalisé.

### Exemple de stratégie

- skill = point d’entrée ;
- subagent = reformulation / spécialisation ;
- MCP = outil métier source de vérité.

### Structure minimale côté plugin

```text
.mcp.json
mcp-server/
```

### Exemple `.mcp.json`

```json
{
  "mcpServers": {
    "fiscal-fr-local": {
      "command": "bash",
      "args": [
        "-lc",
        "cd /chemin/vers/fiscal-fr/mcp-server && npm run dev"
      ]
    }
  }
}
```

### Bonnes pratiques MCP

- commencer par un seul outil ;
- valider la chaîne de bout en bout avant d’ajouter d’autres tools ;
- retourner des structures simples et stables ;
- valider les entrées ;
- éviter de laisser le LLM déduire ce qui devrait être renvoyé par l’outil.

---

## 9. Hooks

Les hooks servent à automatiser certains comportements liés au cycle de vie de Claude Code.

Ils sont utiles pour :
- déclencher des vérifications ;
- imposer un contrôle ;
- lancer une automatisation sur événement.

Pour un MVP métier, ils ne sont généralement pas prioritaires.

---

## 10. LSP

Les LSP servers apportent de l’intelligence de code en temps réel pour des langages non couverts nativement.

Pour un plugin fonctionnel métier, ils ne sont généralement pas nécessaires au départ.

---

## 11. Settings

Un plugin peut embarquer un `settings.json` à la racine.

Exemple :

```json
{
  "agent": "security-reviewer"
}
```

Ce mécanisme permet de faire d’un subagent le comportement par défaut du plugin.

À utiliser avec précaution.

---

## 12. Workflow de développement recommandé

### Étape 1 — plugin minimal
Créer :
- `.claude-plugin/plugin.json`
- un skill simple

### Étape 2 — skill dynamique
Ajouter `$ARGUMENTS`.

### Étape 3 — subagent spécialisé
Extraire une responsabilité précise.

### Étape 4 — premier MCP
Créer un serveur MCP local avec un seul outil.

### Étape 5 — brancher le skill au MCP
Faire du MCP la source de vérité.

### Étape 6 — enrichissement progressif
Ajouter outils, corpus, validations, règles.

---

## 13. Commandes utiles en développement

### Charger un plugin local

```bash
claude --plugin-dir ./fiscal-fr
```

### Recharger plugins / skills / agents

```text
/reload-plugins
```

### Aide

```text
/help
```

### Vérifier les diagnostics

```text
/doctor
```

### Vérifier les MCP

```text
/mcp
```

### Lister skills / agents selon l’interface disponible

```text
/skills
/agents
```

---

## 14. Bonnes pratiques de conception

### 14.1 Découper les responsabilités

Bon découpage :
- skill = orchestration ;
- subagent = analyse spécialisée ;
- MCP = logique métier ;
- corpus = connaissance source.

### 14.2 Commencer petit

Toujours valider :
1. un plugin qui charge ;
2. un skill qui marche ;
3. un subagent utile ;
4. un MCP minimal ;
5. une intégration complète.

### 14.3 Éviter l’overengineering

Ne pas construire dès le début :
- marketplace ;
- hooks complexes ;
- LSP custom ;
- énorme architecture multi-outils.

### 14.4 Faire du MCP la source de vérité métier

Ce point est critique pour les plugins métier :
- le LLM reformule ;
- l’outil tranche ;
- le corpus documente ;
- les règles encodent.

### 14.5 Rendre les sorties stables

Privilégier des sorties structurées et régulières.

Exemple :
- `factsConfirmed`
- `hypotheses`
- `pointsToConfirm`
- `mvpDecision`

### 14.6 Versionner le plugin et son corpus

Toujours versionner :
- le plugin ;
- les schémas ;
- les tools ;
- le corpus métier.

---

## 15. Anti-patterns fréquents

- mettre `skills/` ou `agents/` dans `.claude-plugin/`
- faire un skill monolithique qui remplace toute la logique métier
- utiliser MCP trop tôt avec 10 outils au lieu d’un seul
- ne pas valider les entrées d’un tool
- laisser Claude “inventer” une décision métier alors qu’un outil pourrait la produire
- mélanger prototype local et architecture distribuée trop tôt
- ignorer `/doctor` et les diagnostics plugin

---

## 16. Structure recommandée pour un plugin métier

```text
fiscal-fr/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── assistant-fiscal/
│       └── SKILL.md
├── agents/
│   └── tax-qualifier.md
├── .mcp.json
├── mcp-server/
│   ├── package.json
│   ├── tsconfig.json
│   └── src/
│       └── index.ts
├── corpus/
│   ├── raw/
│   ├── normalized/
│   └── schemas/
└── README.md
```

---

## 17. Recommandation spécifique pour un plugin métier sensible

Pour un domaine comme la fiscalité, la conformité, le juridique ou le financier :

- ne jamais dépendre uniquement du prompt ;
- séparer règles et explications ;
- utiliser des sources officielles ;
- versionner les règles ;
- tracer les décisions ;
- gérer explicitement les cas hors périmètre.

---

## 18. Checklist de validation

### Plugin
- [ ] Le plugin charge via `--plugin-dir`
- [ ] Le manifeste est valide
- [ ] Le namespace est correct

### Skill
- [ ] Le skill apparaît dans `/help`
- [ ] L’invocation fonctionne
- [ ] `$ARGUMENTS` fonctionne

### Subagent
- [ ] Le subagent est visible
- [ ] Son rôle est clair
- [ ] Son format de sortie est stable

### MCP
- [ ] Le serveur démarre
- [ ] `/mcp` montre le serveur
- [ ] Le tool est listé
- [ ] Les entrées sont validées
- [ ] La sortie est structurée

### Produit
- [ ] Le flux principal est testable bout en bout
- [ ] Les limites sont explicites
- [ ] Les cas hors périmètre sont gérés

---

## 19. Références officielles

### Création de plugins
- Claude Code Docs — Create plugins

### Référence technique
- Claude Code Docs — Plugins reference

### Skills
- Claude Code Docs — Extend Claude with skills

### Subagents
- Claude Code Docs — Create custom subagents

### MCP
- Claude Code Docs — Connect Claude Code to tools via MCP

### Hooks
- Claude Code Docs — Automate with hooks

### LSP
- Claude Code Docs — LSP servers / Plugins reference

---

## 20. Ordre de lecture conseillé

1. Create plugins
2. Plugins reference
3. Skills
4. Subagents
5. MCP
6. Hooks
7. LSP si besoin spécifique

---

## 21. Conclusion

La meilleure manière d’apprendre Claude Code plugin development est pratique et incrémentale :

1. plugin minimal ;
2. skill ;
3. skill dynamique ;
4. subagent ;
5. MCP minimal ;
6. intégration réelle ;
7. enrichissement métier.

Pour un plugin métier sérieux, le bon principe est simple :

- **Claude orchestre** ;
- **les agents spécialisent** ;
- **le MCP exécute** ;
- **le corpus documente**.

