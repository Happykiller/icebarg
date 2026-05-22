# Demarrage — FimaDesk sur Claude.ai web

Ouvrir Claude : [https://claude.ai](https://claude.ai).

Le guide d'installation complet est inclus dans le livrable : `claude/claudeai/README.md`.

## Résumé en 2 étapes

### 1. Installer la compétence

- Paramètres → Personnaliser → Compétences → Téléverser une compétence
- Sélectionner `claude/claudeai/fimadesk-v1.1.0.zip`
- La compétence **FimaDesk** apparaît dans la liste ✅

### 2. Connecter le serveur MCP (OAuth2)

- Paramètres → Connecteurs → Ajouter un connecteur personnalisé
- URL : `https://kalifa.happykiller.net/mcp`
- Nom : `FimaDesk`
- Claude.ai ouvre une fenêtre OAuth2 → se connecter → Autoriser ✅

## Démarrer FimaDesk

Dans une nouvelle conversation :

```
Je suis célibataire, salarié. Aide-moi à préparer ma déclaration.
```

## Exemples de démarrage

```
Lance le mode qualification fiscale
```
```
Compare mes options fiscales (PFU vs barème, frais réels vs 10%)
```
```
Liste les justificatifs à réunir pour ma déclaration
```
```
Détecte les points de vigilance dans mon dossier
```
```
Prépare une pré-déclaration avec mes montants
```
```
Estime mon impôt sur le revenu 2026
```
```
Guide-moi écran par écran sur impots.gouv.fr
```
