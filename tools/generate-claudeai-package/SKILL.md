---
name: generate-claudeai-package
description: "Génère le package de distribution Claude.ai (ZIP contenant SKILL.md, REFERENCE.md, README.md) à partir de l'état courant du projet fiscal-fr. Invoquer avec /generate-claudeai-package ou quand l'utilisateur demande de générer/mettre à jour le package grand public, la skill Claude.ai, ou le livrable de distribution."
---

# Génération du package de distribution Claude.ai

Tu dois produire un package ZIP prêt à uploader dans Claude.ai > Personnaliser > Compétences,
qui reflète **l'état courant du projet** (outils MCP, logique d'orchestration, barèmes fiscaux).

## Étape 1 — Lire l'état du projet

Avant de générer quoi que ce soit, collecte les informations sources :

```bash
# 1. Lire l'orchestrateur principal
cat CLAUDE.md

# 2. Lister les outils MCP disponibles
find . -name "*.ts" -o -name "*.js" -o -name "*.py" | xargs grep -l "tool\|Tool\|handler" 2>/dev/null | head -20

# 3. Lire les définitions d'outils (noms, descriptions, paramètres)
find . -path "*/tools/*" -o -path "*/src/*" | xargs grep -l "name\|description" 2>/dev/null | head -10

# 4. Vérifier s'il existe des barèmes/références fiscales
find . -name "*.md" | xargs grep -l "barème\|tranche\|plafond\|taux" 2>/dev/null

# 5. Lire le package.json ou équivalent pour la version
cat package.json 2>/dev/null || cat pyproject.toml 2>/dev/null || echo "no version file"
```

Extrais de ces lectures :
- **Liste des outils** : nom exact, description, paramètres acceptés
- **Logique d'orchestration** : dans quel ordre les outils s'enchaînent, quelles questions poser
- **Connaissances fiscales** : barèmes, plafonds, règles déjà documentés
- **Version du projet** : pour versionner le package généré

## Étape 2 — Lire les templates

```bash
cat tools/generate-claudeai-package/TEMPLATES.md
```

Utilise ces templates comme base structurelle pour chaque fichier output.

## Étape 3 — Générer les trois fichiers

### 3a. claude/claudeai/SKILL.md

Génère ce fichier en remplissant le template SKILL avec :
- La liste réelle des outils MCP et leurs descriptions exactes
- La logique d'orchestration extraite du CLAUDE.md
- Les cas fiscaux couverts par les outils disponibles
- La version actuelle du projet dans le frontmatter

Règles impératives pour la Skill :
- Frontmatter `description` ≤ 200 caractères, décrit les déclencheurs d'activation
- Mode dégradé : si le MCP n'est pas connecté, la Skill guide quand même l'utilisateur
  avec les barèmes de REFERENCE.md
- Toujours inclure un disclaimer de non-responsabilité en fin de réponse fiscale
- Langue : français, ton professionnel mais accessible

### 3b. claude/claudeai/REFERENCE.md

Génère ce fichier en combinant :
- Les barèmes et plafonds trouvés dans le projet
- Les données fiscales manquantes à compléter avec les valeurs de l'année en cours
- Toujours indiquer l'année de référence de chaque donnée

Structure obligatoire :
```
# Référence fiscale française [ANNÉE]
## Barème IR
## Plafonds épargne (PER, PEA, livrets)
## Dispositifs de défiscalisation
## Dates clés
## Sources officielles
```

### 3c. claude/claudeai/README.md

Génère le guide d'installation utilisateur final :
- 3 étapes maximum, pas de jargon technique
- Capture d'écran décrite en texte (chemins de navigation exacts dans Claude.ai)
- Exemple de première question à poser pour valider l'installation
- URL du MCP server copiable directement
- Lien vers le repo GitHub pour les mises à jour

## Étape 4 — Packager en ZIP

```bash
python3 tools/generate-claudeai-package/generate.py
```

Ce script :
1. Vérifie que les 3 fichiers existent dans `claude/claudeai/`
2. Crée `claude/claudeai/fiscal-fr-claudeai-vX.Y.Z.zip` (tracké git)
3. Affiche le checksum SHA256 du ZIP
4. Affiche les instructions de distribution

## Étape 5 — Rapport de génération

À la fin, affiche un résumé structuré :

```
✅ Package généré : claude/claudeai/fiscal-fr-claudeai-vX.Y.Z.zip
📦 Contenu :
   - SKILL.md      (XXX lignes) — orchestrateur
   - REFERENCE.md  (XXX lignes) — barèmes fiscaux
   - README.md     (XXX lignes) — guide utilisateur
🔧 Outils MCP couverts : [liste]
⚠️  Points d'attention :
   - [tout ce qui était manquant ou à compléter manuellement]
📋 Prochaine étape : uploader dans Claude.ai > Personnaliser > Compétences
```

## Règles générales

- Ne jamais halluciner de données fiscales — si une valeur est inconnue ou trop ancienne,
  l'indiquer explicitement avec `[À VÉRIFIER POUR L'ANNÉE EN COURS]`
- Versionner le package avec le numéro de version du projet
- Créer `dist/` s'il n'existe pas
- Ne jamais écraser les fichiers sources du projet
- Si CLAUDE.md a changé depuis la dernière génération, régénérer entièrement