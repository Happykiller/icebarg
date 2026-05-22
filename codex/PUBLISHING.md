# Publication Codex Store - fiscal-fr

Ce dossier contient le candidat de publication Codex marketplace du plugin `fiscal-fr`.

## Structure

```text
publication/codex-store/
  .agents/plugins/marketplace.json
  plugins/fiscal-fr/
    .codex-plugin/plugin.json
    .mcp.json
    README.md
    PRIVACY.md
    TERMS.md
    icon.png
    skills/fiscal-fr/
      SKILL.md
      REFERENCE.md
```

## Etat publication

Statut : candidat publication.

Pret pour revue technique :
- manifeste Codex separe du plugin Claude existant,
- skill autonome issu du package Claude.ai,
- reference fiscale embarquee,
- MCP declare sans token ni secret,
- OAuth2 declare pour la connexion utilisateur,
- marketplace local de publication fourni.

Reste a confirmer avant soumission publique :
- canal officiel de soumission Codex Store,
- validation OAuth2 effective dans l'IHM Codex,
- URLs finales de politique de confidentialite et conditions d'utilisation,
- eventuels screenshots marketplace si requis,
- verification annuelle des points fiscaux marques a confirmer.

## Commandes de verification

Verifier les JSON :

```powershell
Get-Content .\publication\codex-store\.agents\plugins\marketplace.json | ConvertFrom-Json
Get-Content .\publication\codex-store\plugins\fiscal-fr\.codex-plugin\plugin.json | ConvertFrom-Json
Get-Content .\publication\codex-store\plugins\fiscal-fr\.mcp.json | ConvertFrom-Json
```

Verifier l'absence de token avec un scan adapte a votre environnement :

```powershell
Get-ChildItem .\publication\codex-store -Recurse -File -Force |
  Select-String -Pattern '<motifs de secrets a verifier>'
```

## Notes de securite

Le package ne doit jamais contenir de token utilisateur, secret OAuth2 ou configuration locale privee.
La logique fiscale deterministe doit rester dans le serveur MCP externe.
