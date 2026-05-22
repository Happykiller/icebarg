# Politique de confidentialite - FimaDesk

`FimaDesk` est un plugin d'assistance a la preparation de declaration de revenus francaise.

## Donnees traitees

Le plugin peut traiter les informations fiscales que l'utilisateur fournit volontairement dans la conversation, notamment :

- situation familiale,
- personnes a charge,
- types de revenus,
- charges et reductions,
- montants declares,
- documents ou points de vigilance mentionnes par l'utilisateur.

## Serveur MCP

Les calculs et qualifications deterministes sont delegues au serveur MCP externe :

```text
https://kalifa.happykiller.net/mcp
```

L'authentification est declaree via OAuth2.
Le package du plugin ne contient aucun token utilisateur.

## Stockage

Le plugin lui-meme ne persiste pas de donnees fiscales dans ses fichiers.
Les donnees d'authentification et les traitements cote serveur dependent de l'infrastructure MCP externe.

## Limites

`FimaDesk` ne remplace pas un expert-comptable, un avocat fiscaliste ou l'administration fiscale.
Les estimations sont indicatives et non opposables.

## Contact

Fabrice Rosito - fabrice.rosito@gmail.com
