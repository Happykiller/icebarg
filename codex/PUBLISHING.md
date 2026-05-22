# Publication Codex Store - fiscal-fr

Ce dossier contient le candidat de publication Codex marketplace du plugin `fiscal-fr`.

## Structure

```text
codex/
  PUBLISHING.md                   (ce fichier)
  SUBMISSION_CHECKLIST.md
  CHANGELOG.md
  plugin/
    .codex-plugin/plugin.json
    .mcp.json
    README.md
    PRIVACY.md
    TERMS.md
    icon.png
    skills/fiscal-fr/
      SKILL.md
      REFERENCE.md

.agents/plugins/marketplace.json  (registry marketplace local, racine repo)
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
Get-Content .\codex\plugin\.codex-plugin\plugin.json | ConvertFrom-Json
Get-Content .\codex\plugin\.mcp.json | ConvertFrom-Json
Get-Content .\.agents\plugins\marketplace.json | ConvertFrom-Json
```

```bash
python3 -c "import json; json.load(open('codex/plugin/.codex-plugin/plugin.json')); print('OK')"
python3 -c "import json; json.load(open('codex/plugin/.mcp.json')); print('OK')"
python3 -c "import json; json.load(open('.agents/plugins/marketplace.json')); print('OK')"
```

Verifier l'absence de token :

```bash
grep -r "Bearer\|token\|secret\|password" codex/plugin/ --include="*.json" --include="*.md"
```

## Notes de securite

Le package ne doit jamais contenir de token utilisateur, secret OAuth2 ou configuration locale privee.
La logique fiscale deterministe doit rester dans le serveur MCP externe.
