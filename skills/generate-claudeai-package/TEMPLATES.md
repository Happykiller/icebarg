# Templates de génération

Ces templates définissent la structure des fichiers output.
Remplace tous les placeholders `{{...}}` avec les données extraites du projet.

---

## Template SKILL.md

```markdown
---
name: fiscal-fr
description: "Assistant fiscal français : calcul IR, optimisation PER, Pinel, frais réels. Active-toi pour toute question sur impôts, déclaration, défiscalisation ou optimisation fiscale."
version: {{VERSION}}
updated: {{DATE_ISO}}
---

# Assistant fiscal français

Tu es un assistant spécialisé en fiscalité française pour les particuliers.
Tu aides à comprendre, calculer et optimiser la situation fiscale de l'utilisateur.

> ⚠️ Disclaimer : cet assistant est un outil d'aide à la compréhension fiscale.
> Il ne remplace pas un expert-comptable ou un conseiller fiscal agréé.
> Les calculs sont indicatifs et basés sur la législation en vigueur au moment
> de la dernière mise à jour ({{DATE_LISIBLE}}).

## Outils disponibles

{{#each OUTILS}}
### `{{nom}}`
{{description}}
Paramètres : {{parametres}}

{{/each}}

## Orchestration — Comment guider l'utilisateur

### Diagnostic initial
Quand l'utilisateur pose une question fiscale sans contexte,
pose ces questions dans cet ordre (pas toutes d'un coup) :
1. Situation familiale (célibataire, marié(e), pacsé(e), nombre d'enfants)
2. Revenus principaux (salaire, indépendant, retraite)
3. Dispositifs en cours (Pinel, PER, immobilier locatif)

### Séquences d'orchestration

{{ORCHESTRATION_SEQUENCES}}

### Mode dégradé (sans MCP connecté)
Si les outils MCP ne sont pas disponibles, utilise les barèmes
de REFERENCE.md pour répondre avec des calculs manuels.
Indique à l'utilisateur comment connecter le MCP pour des calculs automatisés.

## Format des réponses

- Toujours donner un chiffre concret avant une explication
- Structurer : Résultat → Explication → Conseil d'optimisation
- Pour les montants > 1000€ : format `X XXX €`
- Terminer par le disclaimer si la réponse implique un conseil fiscal
```

---

## Template REFERENCE.md

```markdown
# Référence fiscale française {{ANNEE}}

> Données valables pour la déclaration de revenus {{ANNEE}}
> (revenus perçus en {{ANNEE_REVENUS}}).
> Sources : impots.gouv.fr, service-public.fr

## Barème IR {{ANNEE}}

| Tranche de revenu net imposable | Taux |
|---|---|
| Jusqu'à {{TRANCHE_0}} € | 0% |
| De {{TRANCHE_0}} € à {{TRANCHE_1}} € | 11% |
| De {{TRANCHE_1}} € à {{TRANCHE_2}} € | 30% |
| De {{TRANCHE_2}} € à {{TRANCHE_3}} € | 41% |
| Au-delà de {{TRANCHE_3}} € | 45% |

**Quotient familial** : {{QF_DEMI_PART}} € par demi-part supplémentaire (plafond)

## Plafonds épargne

### PER (Plan Épargne Retraite)
- Plafond déductible : **10% des revenus professionnels** dans la limite de {{PER_PLAFOND_MAX}} €
- Plafond alternatif (sans revenus) : {{PER_PLAFOND_MIN}} €
- Versements non déduits : ouvrent droit à exonération à la sortie

### PEA
- Plafond versements : {{PEA_PLAFOND}} €
- PEA-PME : {{PEA_PME_PLAFOND}} € supplémentaires

### Livrets réglementés
| Livret | Taux | Plafond |
|---|---|---|
| Livret A | {{LIVRET_A_TAUX}}% | {{LIVRET_A_PLAFOND}} € |
| LDDS | {{LDDS_TAUX}}% | {{LDDS_PLAFOND}} € |
| LEP | {{LEP_TAUX}}% | {{LEP_PLAFOND}} € |

## Dispositifs de défiscalisation

### Pinel
{{PINEL_REGLES}}

### Frais réels vs forfait
- Déduction forfaitaire automatique : **10%** des salaires bruts
- Minimum : {{FRAIS_REELS_MIN}} € / Maximum : {{FRAIS_REELS_MAX}} €
- Opter pour les frais réels si dépenses réelles > déduction forfaitaire

## Dates clés {{ANNEE}}

| Événement | Date |
|---|---|
| Ouverture déclaration en ligne | {{DATE_OUVERTURE}} |
| Clôture départements 1-19 | {{DATE_CLOTURE_1}} |
| Clôture départements 20-54 | {{DATE_CLOTURE_2}} |
| Clôture départements 55-976 | {{DATE_CLOTURE_3}} |
| Avis d'imposition disponibles | {{DATE_AVIS}} |

## Sources officielles
- Déclaration en ligne : https://www.impots.gouv.fr
- Barèmes officiels : https://www.service-public.fr/particuliers/vosdroits/F1419
- Simulateur officiel : https://www.impots.gouv.fr/simulateur-ir
```

---

## Template README.md

```markdown
# Assistant fiscal français pour Claude.ai

Cet assistant t'aide à comprendre et optimiser ta situation fiscale française
directement dans Claude.ai.

**Version :** {{VERSION}} — **Mis à jour :** {{DATE_LISIBLE}}

## Installation en 3 étapes

### Étape 1 — Connecter le serveur de calcul (MCP)

1. Dans Claude.ai, clique sur ton avatar en haut à droite → **Paramètres**
2. Va dans **Connecteurs** → **Ajouter un connecteur personnalisé**
3. Dans le champ URL, colle :
   ```
   {{MCP_URL}}
   ```
4. Donne-lui le nom `Fiscal FR` et clique **Ajouter**

> 💡 **Plan Free ?** Tu as droit à 1 connecteur personnalisé.
> L'assistant fonctionne aussi sans connecteur (calculs manuels),
> mais les résultats seront moins précis.

### Étape 2 — Installer la compétence

1. Dans **Paramètres** → **Personnaliser** → **Compétences**
2. Clique **Téléverser une compétence**
3. Sélectionne le fichier `fiscal-fr-claudeai-{{VERSION}}.zip`
4. La compétence apparaît dans ta liste ✅

### Étape 3 — Tester l'installation

Démarre une nouvelle conversation et pose cette question :

> *"Peux-tu faire un diagnostic fiscal de ma situation ? Je suis [célibataire/marié(e)],
> je gagne environ [ton salaire]€ par an."*

Claude doit activer automatiquement l'assistant fiscal et te poser
des questions complémentaires.

## Ce que l'assistant peut faire

{{#each OUTILS}}
- **{{nom_lisible}}** : {{description_courte}}
{{/each}}

## Mise à jour

Pour mettre à jour vers une nouvelle version :
1. Télécharge le nouveau ZIP depuis {{REPO_URL}}/releases
2. Dans Paramètres → Compétences, supprime l'ancienne version
3. Uploade le nouveau ZIP

## Limitations

- Les calculs sont indicatifs — toujours vérifier avec impots.gouv.fr
- Données fiscales valables pour {{ANNEE}} — vérifier en cas de changement de loi
- Ne remplace pas un expert-comptable pour les situations complexes

## Problèmes fréquents

**L'assistant ne s'active pas automatiquement**
→ Essaie de mentionner explicitement "fiscal" ou "impôts" dans ta question

**Le connecteur MCP ne se connecte pas**
→ Vérifie que ton plan Claude supporte les connecteurs (Free = 1 max)
→ Essaie de retirer et re-ajouter le connecteur

**Les calculs semblent incorrects**
→ Vérifie la version de la compétence — une mise à jour est peut-être disponible

---
*Projet open source : {{REPO_URL}}*
*Signaler un problème : {{REPO_URL}}/issues*
```