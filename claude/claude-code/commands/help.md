---
description: Guide rapide du plugin FimaDesk (modes, checks, depannage)
---

# FimaDesk: aide rapide

Tu aides l'utilisateur a demarrer rapidement avec le plugin FimaDesk.

Donne une reponse courte et pratique avec ces sections :

1. Commandes utiles
   - `/fimadesk:help`
   - `/fimadesk:start [mode]`
   - `/fimadesk:infos`
   - `/fimadesk:assistant-fiscal [mode]`

2. Modes disponibles
   - qualification
   - justificatifs
   - vigilance
   - predeclaration
   - estimation
   - copilote

3. Verification rapide
   - `/reload-plugins`
   - `/help`
   - `/mcp`

4. Depannage MCP
   - Verifier que le token est bien renseigne dans `.mcp.json` (pas `change-me`).
   - Verifier que le connecteur `fimadesk` apparait bien dans `/mcp`.
   - Si besoin: relancer Claude avec `claude --plugin-dir ./claude/claude-code`, puis `/reload-plugins`.

Termine avec: "Dis-moi ton mode et ta situation en 1 phrase, je te lance le bon parcours."
