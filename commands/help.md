---
description: Guide rapide du plugin fiscal-fr (modes, checks, depannage)
---

# fiscal-fr: aide rapide

Tu aides l'utilisateur a demarrer rapidement avec le plugin fiscal-fr.

Donne une reponse courte et pratique avec ces sections :

1. Commandes utiles
   - `/fiscal-fr:help`
   - `/fiscal-fr:start [mode]`
   - `/fiscal-fr:infos`
   - `/fiscal-fr:assistant-fiscal [mode]`

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
   - Verifier que le connecteur `fiscal-fr` apparait bien dans `/mcp`.
   - Si besoin: relancer Claude depuis le dossier parent avec `claude --plugin-dir ./fiscal-fr`, puis `/reload-plugins`.

Termine avec: "Dis-moi ton mode et ta situation en 1 phrase, je te lance le bon parcours."
