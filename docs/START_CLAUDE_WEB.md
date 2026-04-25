# Demarrage — Claude.ai web

Ouvrir Claude : [https://claude.ai](https://claude.ai).

## 1. Recuperer le fichier des competences

Au prealable, recuperer le fichier zip des competences disponible dans le dossier `delivery/` du repository :

[`delivery/`](../delivery/)

Télécharger le fichier `.zip` correspondant à la version la plus récente.

## 2. Importer la competence

- Dans le menu de gauche, cliquer sur `Personaliser`.
- Ouvrir le sous-menu `Competences`.
- Cliquer sur `+`, puis `Creer une competence`, puis `Televerser une competence`.
- Dans la fenetre qui s'ouvre, selectionner le fichier zip des competences telecharge au prealable.

La competence `fisk-assistant` apparait alors dans la liste des competences.

## 3. Ajouter le connecteur MCP

- Retourner dans le menu de gauche sur `Connecteurs`.
- Cliquer sur `+`, puis `Ajouter un connecteur personnalise`.
- Indiquer un nom (par exemple `Assistant Fiscal`).
- Indiquer l'URL MCP :

```
https://kalifa.happykiller.net/mcp
```

- Dans la liste des connecteurs, choisir `Assistant Fiscal`.
- Cliquer sur `Se connecter` : cela ouvre la page d'authentification de l'assistant fiscal.

## 4. S'authentifier

- Utiliser l'identifiant et le mot de passe fournis par l'administrateur (Fabrice).
- Valider avec `Autoriser`.
- En cas de succes, retour automatique sur Claude.ai.

Tout est pret. Vous pouvez demarrer l'assistant fiscal dans une nouvelle conversation.

Exemple :

```
Je suis celibataire, salarie. Aide-moi a preparer ma declaration.
```

## Exemples de demarrage

```
Qualifie ma situation fiscale
```
```
Compare mes options fiscales (PFU vs bareme, frais reels vs 10%)
```
```
Liste les justificatifs a reunir pour ma declaration
```
```
Detecte les points de vigilance dans mon dossier
```
```
Prepare une pre-declaration avec mes montants
```
```
Estime mon impot sur le revenu 2026
```
```
Guide-moi ecran par ecran sur impots.gouv.fr
```
