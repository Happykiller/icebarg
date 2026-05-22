# fiscal-fr pour Codex

Package Codex marketplace du plugin `fiscal-fr`.

Ce dossier est volontairement separe du plugin Claude Code existant afin de limiter les regressions sur les fichiers historiques du depot.

## Contenu

- `.codex-plugin/plugin.json` : manifeste Codex marketplace.
- `.mcp.json` : connexion au serveur MCP fiscal externe, sans token embarque.
- `skills/fiscal-fr/SKILL.md` : skill utilisateur autonome, adapte depuis le package Claude.ai.
- `skills/fiscal-fr/REFERENCE.md` : references fiscales et points a confirmer.
- `icon.png` : icone du plugin.

## Connexion MCP

Le serveur MCP est declare sur :

```text
https://kalifa.happykiller.net/mcp
```

L'authentification est declaree en OAuth2 dans `.mcp.json`.
Le plugin ne doit pas embarquer de token, ni de secret utilisateur, dans ses fichiers.

## Outils MCP attendus

- `qualify_tax_profile`
- `list_supporting_documents`
- `detect_review_points`
- `build_pre_declaration`
- `estimate_impact`
- `compare_tax_options`
- `guide_filing_step`

## Limites

Le skill orchestre les echanges et la restitution utilisateur.
La logique fiscale deterministe doit rester dans le serveur MCP externe.

Les cas marques `human_review`, les donnees insuffisantes et les points a confirmer doivent toujours etre exposes a l'utilisateur.
