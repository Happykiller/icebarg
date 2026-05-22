# Plan implementation MVP

Etat de reference du MVP pour ce repository (extraction plugin Claude uniquement).

## Contexte

Le POC initial melangeait plugin Claude et serveur MCP local.
Dans ce repository, le scope est :
- plugin Claude Code (`claude/claude-code/` — `.claude-plugin`, `skills`, `agents`, `commands`),
- skill Claude.ai (`claude/claudeai/`),
- plugin Codex (`codex/plugin/`),
- configuration MCP distante via `.mcp.json` (local, gitignore).

Le code du serveur MCP n'est pas embarque ici.

## Phases MVP

| Phase | Statut | Notes |
|---|---|---|
| Structure plugin minimale | DONE | `claude/claude-code/.claude-plugin/`, `commands/`, `agents/` |
| Orchestrateur skill principal | DONE | `claude/claude-code/skills/assistant-fiscal/SKILL.md` |
| Agents specialises | DONE | `tax-qualifier`, `documents-checklist`, `review-points` |
| Demarrage Claude Code/Web | DONE | docs de demarrage presentes |
| Coherence documentaire extraction POC | DONE | references POC locales supprimees/ajustees |
| Reorganisation multi-cibles | DONE | `claude/`, `codex/`, `tools/` — structure cible en place |
| Validation packaging Web | PARTIAL | skill Claude.ai dans `claude/claudeai/`, procedure zip a valider |

## Reste a faire MVP

1. Valider le packaging Claude.ai : `python3 tools/generate-claudeai-package/generate.py`.
2. Ajouter une check-list de smoke test manuelle (commands + skill + connexion MCP).
3. Valider en environment reel la sequence complete `qualification -> copilote`.
