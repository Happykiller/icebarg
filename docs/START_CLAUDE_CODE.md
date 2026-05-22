# Demarrage — Claude Code (CLI / desktop)

## 1. Cloner le repository

Depuis un terminal :

```bash
git clone https://github.com/Happykiller/icebarg
cd icebarg
```

## 2. Créer votre fichier de configuration MCP (obligatoire)

Le fichier `.mcp.json` n'est pas versionné (il contient vos credentials).
Créez-le à partir du modèle fourni dans le dossier plugin :

```bash
cp claude/claude-code/.mcp.json.example .mcp.json
```

Puis ouvrir `.mcp.json` et remplacer `<YOUR_TOKEN>` par votre token :

```json
"Authorization": "Bearer <votre-token>"
```

Comment obtenir le token — deux méthodes au choix :

**Méthode A — Page web (recommandée)**

1. Ouvrir dans un navigateur : `https://kalifa.happykiller.net/token-portal`
2. Saisir votre email et mot de passe.
3. Copier le token affiché (bouton "Copier le token").
4. Coller ce token à la place de `<YOUR_TOKEN>` dans `.mcp.json`.

**Méthode B — Requête API (terminal / script)**

```bash
curl -s -X POST https://kalifa.happykiller.net/token-portal \
  -H "Accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=vous@exemple.com&password=votre-mot-de-passe"
```

Réponse :

```json
{ "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." }
```

Extraire directement le token (nécessite `jq`) :

```bash
TOKEN=$(curl -s -X POST https://kalifa.happykiller.net/token-portal \
  -H "Accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=vous@exemple.com&password=votre-mot-de-passe" | jq -r '.token')
```

Le token est valable 365 jours.

> Si vous n'avez pas encore de compte, rapprochez-vous de l'admin.

Ne modifiez pas l'URL MCP si elle est deja renseignee (`https://kalifa.happykiller.net/mcp`).

## 3. Lancer Claude Code

- Ouvrir un terminal.
- Se placer dans le dossier `icebarg` (racine du repo clone).
- Executer :

```bash
claude --plugin-dir ./claude/claude-code
```

## 4. Verifier que le plugin est actif

```text
/help
```

Le skill doit apparaitre : `/fiscal-fr:assistant-fiscal`.

Verification du connecteur MCP :

```text
/mcp
```

Si les commandes n'apparaissent pas :

```text
/reload-plugins
```

## 5. Demarrer l'assistant fiscal

```text
/fiscal-fr:assistant-fiscal
```

Ou directement en langage naturel :

```
Je suis celibataire, salarie. Aide-moi a preparer ma declaration.
```

## Commandes utiles

```text
/fiscal-fr:assistant-fiscal [mode]
/fiscal-fr:start [mode]
/fiscal-fr:help
/fiscal-fr:infos
```

## Note developpement

Les commandes de developpement (install, dev, build, tests) restent documentees dans le [README general](../README.md).
