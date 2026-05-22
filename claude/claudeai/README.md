# Assistant fiscal français pour Claude.ai

Cet assistant t'aide à comprendre et optimiser ta situation fiscale française
directement dans Claude.ai.

**Version :** 1.0.0 — **Mis à jour :** 22 mai 2026

## Installation en 3 étapes

### Étape 1 — Connecter le serveur de calcul (MCP)

1. Dans Claude.ai, clique sur ton avatar en haut à droite → **Paramètres**
2. Va dans **Connecteurs** → **Ajouter un connecteur personnalisé**
3. Dans le champ URL, colle :
   ```
   https://kalifa.happykiller.net/mcp
   ```
4. Pour obtenir ton token, rends-toi sur : `https://kalifa.happykiller.net/token-portal`
5. Renseigne ton email et mot de passe → copie le token affiché
6. Dans le champ Authorization, renseigne : `Bearer <ton-token>`
7. Donne-lui le nom `Fiscal FR` et clique **Ajouter**

> 💡 **Plan Free ?** Tu as droit à 1 connecteur personnalisé.
> L'assistant fonctionne aussi sans connecteur (calculs manuels depuis REFERENCE.md),
> mais les résultats seront moins précis.

### Étape 2 — Installer la compétence

1. Dans **Paramètres** → **Personnaliser** → **Compétences**
2. Clique **Téléverser une compétence**
3. Sélectionne le fichier `fiscal-fr-claudeai-1.0.0.zip`
4. La compétence apparaît dans ta liste ✅

### Étape 3 — Tester l'installation

Démarre une nouvelle conversation et pose cette question :

> *"Peux-tu faire un diagnostic fiscal de ma situation ? Je suis célibataire,
> je gagne environ 45 000 € par an."*

Claude doit activer automatiquement l'assistant fiscal et te poser
des questions complémentaires sur ta situation.

## Ce que l'assistant peut faire

| Mode | Comment l'activer | Ce que ça fait |
|------|-------------------|----------------|
| **Qualification** | "Lance le mode qualification" | Qualifie ta situation fiscale, classe en simple / à surveiller / hors périmètre |
| **Arbitrages** | "Compare mes options fiscales" | Compare PFU vs barème, frais réels vs 10%, micro-foncier vs réel, rattachement vs pension |
| **Justificatifs** | "Passe en mode justificatifs" | Liste les documents obligatoires, recommandés, manquants |
| **Vigilance** | "Détecte les points de vigilance" | Repère les incohérences, régimes à trancher, cas hors périmètre |
| **Pré-déclaration** | "Prépare une pré-déclaration" | Produit un brouillon structuré avec codes cases et origines tracées |
| **Estimation** | "Estime mon impôt" | Estimation indicative IR 2026 (barème progressif, quotient familial, décote, réductions/crédits) |
| **Copilote** | "Guide-moi écran par écran" | Copilote de saisie sur impots.gouv.fr, étape par étape |

## Mise à jour

Pour mettre à jour vers une nouvelle version :
1. Télécharge le nouveau ZIP depuis https://github.com/happykiller/icebarg/releases
2. Dans Paramètres → Compétences, supprime l'ancienne version
3. Uploade le nouveau ZIP

## Limitations

- Les calculs sont indicatifs — toujours vérifier avec impots.gouv.fr
- Données fiscales valables pour 2026 — vérifier en cas de changement de loi
- Ne remplace pas un expert-comptable pour les situations complexes
- Cas hors périmètre : revenus étrangers, crypto-actifs, activités BIC/BNC complexes

## Problèmes fréquents

**L'assistant ne s'active pas automatiquement**
→ Essaie de mentionner explicitement "fiscal" ou "impôts" dans ta question

**Le connecteur MCP ne se connecte pas**
→ Vérifie que ton plan Claude supporte les connecteurs (Free = 1 max)
→ Obtiens un token sur https://kalifa.happykiller.net/token-portal
→ Essaie de retirer et re-ajouter le connecteur

**Les calculs semblent incorrects**
→ Vérifie la version de la compétence — une mise à jour est peut-être disponible

---
*Projet open source : https://github.com/happykiller/icebarg*
*Signaler un problème : https://github.com/happykiller/icebarg/issues*
