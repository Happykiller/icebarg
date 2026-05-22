# Assistant fiscal français pour Claude.ai

Cet assistant t'aide à comprendre et optimiser ta situation fiscale française
directement dans Claude.ai.

**Version :** 1.1.0 — **Mis à jour :** 22 mai 2026

---

## Installation en 2 étapes

### Étape 1 — Installer la compétence

1. Dans Claude.ai, clique sur ton avatar → **Paramètres** → **Personnaliser** → **Compétences**
2. Clique **Téléverser une compétence**
3. Sélectionne le fichier `fiscal-fr-claudeai-v1.1.0.zip`
4. La compétence apparaît dans ta liste ✅

### Étape 2 — Connecter le serveur de calcul (MCP)

Le connecteur permet d'activer les calculs fiscaux déterministes (qualifications, arbitrages, estimations).

1. Dans **Paramètres** → **Connecteurs** → **Ajouter un connecteur personnalisé**
2. Dans le champ URL, colle :
   ```
   https://kalifa.happykiller.net/mcp
   ```
3. Donne-lui le nom `Fiscal FR` et clique **Ajouter**
4. Claude.ai ouvre une fenêtre d'autorisation OAuth2 — connecte-toi avec ton email et mot de passe
5. Clique **Autoriser** → le connecteur passe au statut ✅ Connecté

> 💡 **Pas de compte ?** Rapproche-toi de l'admin pour en créer un.
>
> 💡 **Plan Free ?** Tu as droit à 1 connecteur personnalisé gratuit.
> L'assistant fonctionne aussi sans connecteur (calculs manuels via les barèmes intégrés),
> mais les résultats seront moins précis.

---

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

---

## Tester l'installation

Démarre une nouvelle conversation et pose cette question :

> *"Peux-tu faire un diagnostic fiscal de ma situation ? Je suis célibataire,
> je gagne environ 45 000 € par an."*

Claude doit activer automatiquement l'assistant fiscal et te poser
des questions complémentaires.

---

## Mise à jour

Pour mettre à jour vers une nouvelle version :
1. Télécharge le nouveau ZIP depuis https://github.com/happykiller/icebarg/releases
2. Dans Paramètres → Compétences, supprime l'ancienne version
3. Uploade le nouveau ZIP

> Le connecteur MCP n'est pas à reconfigurer lors d'une mise à jour de compétence.

---

## Limitations

- Les calculs sont indicatifs — toujours vérifier avec impots.gouv.fr
- Données fiscales valables pour 2026 — vérifier en cas de changement de loi
- Ne remplace pas un expert-comptable pour les situations complexes
- Cas hors périmètre : revenus étrangers, crypto-actifs, activités BIC/BNC complexes

---

## Problèmes fréquents

**L'assistant ne s'active pas automatiquement**
→ Essaie de mentionner explicitement "fiscal" ou "impôts" dans ta question

**La fenêtre OAuth2 ne s'ouvre pas**
→ Vérifie que les popups ne sont pas bloqués par ton navigateur
→ Réessaie depuis Paramètres → Connecteurs → icône de reconnexion

**Le connecteur s'affiche comme déconnecté**
→ Clique sur le connecteur → **Reconnecter** — la session OAuth2 a peut-être expiré

**Les calculs semblent incorrects**
→ Vérifie la version de la compétence — une mise à jour est peut-être disponible

---

*Projet open source : https://github.com/happykiller/icebarg*
*Signaler un problème : https://github.com/happykiller/icebarg/issues*
