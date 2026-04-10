# Plan implementation MVP

Etat de reference du MVP pour ce repository (extraction plugin Claude uniquement).

## Contexte

Le POC initial melangeait plugin Claude et serveur MCP local.
Dans ce repository, le scope est :
- plugin Claude (`.claude-plugin`, `skills`, `agents`, `commands`, `docs`),
- configuration MCP distante via `.mcp.json`.

Le code du serveur MCP n'est pas embarque ici.

## Phases MVP

| Phase | Statut | Notes |
|---|---|---|
| Structure plugin minimale | DONE | `plugin.json`, `commands/`, `agents/` presents |
| Orchestrateur skill principal | DONE | `skills/assistant-fiscal/SKILL.md` present |
| Agents specialises | DONE | `tax-qualifier`, `documents-checklist`, `review-points` |
| Demarrage Claude Code/Web | DONE | docs de demarrage presentes |
| Coherence documentaire extraction POC | DONE | references POC locales supprimees/ajustees |
| Validation packaging Web | PARTIAL | zip present (`delivery/`), procedure de regeneration a formaliser |

## Reste a faire MVP

1. Ajouter une procedure standard de release zip (`delivery/`) versionnee.
2. Ajouter une check-list de smoke test manuelle (commands + skill + connexion MCP).
3. Valider en environment reel la sequence complete `qualification -> copilote`.
