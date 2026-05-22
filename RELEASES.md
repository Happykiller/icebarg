# Releases — fiscal-fr

Tracker des versions publiées par cible de distribution.

## Cibles de distribution

| Cible | Dossier source | Livrable |
|-------|---------------|---------|
| **Claude Code** | Racine du repo (`.claude-plugin/`, `skills/`, `agents/`, `commands/`) | Installation directe via CLI |
| **Claude.ai** (web) | `claude/claudeai/` | ZIP généré dans `dist/` (gitignored), uploadé dans Claude.ai > Personnaliser > Compétences |
| **Codex** | `codex/plugin/` | Soumission store Codex via `.agents/plugins/marketplace.json` |

Pour générer le package Claude.ai : invoquer le skill `/generate-claudeai-package`.

## Historique

| Version | Date | Claude Code | Claude.ai | Codex | Notes |
|---------|------|-------------|-----------|-------|-------|
| 1.1.0 | 2026-05-22 | racine repo | `claude/claudeai/` | `codex/plugin/` | Réorganisation multi-cibles |
| 1.0.0 | 2024-04-08 | Initial commit | `fisk-assistant_1.0.0.zip` (archivé) | — | POC initial |

## Procédure de release

### Claude Code
Installation directe depuis ce repository — pas de zip à générer.
La commande `/start` déclenche le skill `assistant-fiscal`.

### Claude.ai
1. Mettre à jour `VERSION`.
2. Éditer `claude/claudeai/SKILL.md` et `claude/claudeai/REFERENCE.md` si besoin.
3. Lancer `/generate-claudeai-package` → crée `dist/fiscal-fr-claudeai-vX.Y.Z.zip`.
4. Uploader le ZIP dans Claude.ai > Personnaliser > Compétences.
5. Connecter le MCP via l'URL OAuth2 (voir `claude/claudeai/README.md`).
6. Noter la version et la date dans ce fichier.

### Codex
1. Vérifier la checklist `codex/SUBMISSION_CHECKLIST.md`.
2. Vérifier les JSON avec les commandes documentées dans `codex/PUBLISHING.md`.
3. Scanner l'absence de secrets.
4. Soumettre via le canal officiel Codex Store (à confirmer).
5. Noter la version et la date dans ce fichier.
