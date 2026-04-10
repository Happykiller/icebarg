# AGENTS.md

Ce fichier décrit les agents du plugin Claude Code `fiscal-fr` et les conventions de rédaction.

## Sources de vérité documentaire

Pour éviter les écarts entre produit, implémentation et agents, appliquer cette hiérarchie :

1. `README.md` : référence fonctionnelle (périmètre utilisateur, cas couverts, limites).
2. `docs/roadmaps/PLAN_IMPLEMENTATION_MVP.md` : référence d'exécution MVP (phases, statut DONE|PARTIAL|TODO, reste à faire).
   `docs/roadmaps/PLAN_IMPLEMENTATION_MATURITE.md` : référence d'exécution post-MVP (lots de maturité).
3. `assets/AGENT_IMPLEMENTATION_GUIDE.md` : aide pratique pour créer/faire évoluer un agent Claude.
4. `assets/MCP_CONSUMER_INTERFACE_CONTRACT.md` : contrat d'interface MCP à respecter côté plugin (outils, payloads, erreurs, séquence d'appel).

Quand le périmètre fonctionnel change, mettre à jour **README + plan** dans la même PR.

## Objectif du projet

`fiscal-fr` est un plugin d'assistance à la préparation de déclaration de revenus française.

Notre vision s'articule autour de trois axes fondamentaux que chaque agent doit respecter :

1.  **Assister** : Aider, guider et accompagner le déclarant. Simplifier la complexité administrative.
2.  **Conseiller** : Apporter une expertise pour optimiser les droits du déclarant. Maximiser la valeur monétaire du résultat.
3.  **Rapidité** : Faire gagner du temps. Supprimer les recherches fastidieuses et fluidifier la saisie.

Le plugin s'appuie sur :
- un orchestrateur (skill `assistant-fiscal`),
- des agents spécialisés (dossier `agents/`),
- une configuration MCP (`.mcp.json`) qui connecte les tools fiscaux.

## Emplacement des agents

Chaque agent spécialisé vit dans `agents/<nom-agent>.md`.

Exemple actuel :
- `agents/tax-qualifier.md`
- `agents/documents-checklist.md`
- `agents/review-points.md`

## Contrat d'un agent

Chaque fichier agent doit inclure :
- un frontmatter YAML (`name`, `description`, `tools`, `model`),
- une section `Mission` claire,
- un périmètre explicite (ce que l'agent fait / ne fait pas),
- un format de sortie imposé quand nécessaire.

## Conventions de conception

- **Périmètre strict** : un agent ne doit traiter qu'un sous-problème précis.
- **Pas de sur-promesse** : ne jamais prétendre couvrir un cas complexe non supporté.
- **Traçabilité** : distinguer faits, hypothèses et points à confirmer.
- **Sécurité métier** : pas de calcul fiscal inventé, pas de conseil définitif hors périmètre.
- **Sortie actionnable** : produire des résultats structurés, exploitables par l'orchestrateur.
- **Séparation affichage/valeur** : distinguer les libellés lisibles utilisateur des codes/valeurs techniques MCP (enum, codes de cases, identifiants formulaires).

## Consignes produit et UX à respecter

- **Progressivité** : ne pas poser 100 questions d'un coup, avancer par étapes.
- **Transparence** : toujours distinguer faits, hypothèses, points à confirmer.
- **Refus propre** : signaler clairement les cas hors périmètre et recommander revue humaine.
- **Discipline outillée** : la logique fiscale déterministe doit vivre dans les tools MCP, pas dans des suppositions LLM.
- **Ton** : professionnel, rassurant, structuré, non juridique, non verbeux.

## Orchestration attendue

Le skill `skills/assistant-fiscal/SKILL.md` pilote les interactions utilisateur.

Pour la qualification fiscale, l'orchestrateur doit s'appuyer sur `tax-qualifier` avant de conclure.
Pour la phase justificatifs, l'orchestrateur doit s'appuyer sur `documents-checklist` apres appel de `list_supporting_documents`.
Pour la phase points de vigilance, l'orchestrateur doit s'appuyer sur `review-points` apres appel de `detect_review_points`.

L'orchestrateur doit suivre le fil conversationnel cible :

1. cadrage,
2. qualification,
3. justificatifs,
4. points de vigilance,
5. pré-déclaration,
6. estimation indicative,
7. copilote de saisie,
8. contrôle final.

## Ajouter un nouvel agent

1. Créer `agents/<nouvel-agent>.md`.
2. Définir un rôle spécialisé et non redondant.
3. Décrire explicitement les limites et cas hors périmètre.
4. Définir un format de sortie clair et stable.
5. Mettre à jour le skill orchestrateur si ce nouvel agent doit être invoqué.
6. Mettre à jour la documentation associée si le périmètre fonctionnel est impacté (`README.md`, `docs/roadmaps/PLAN_IMPLEMENTATION_MVP.md`, et `docs/roadmaps/PLAN_IMPLEMENTATION_MATURITE.md` si post-MVP).

## Architecture MCP du repository — règle obligatoire

Ce repository contient le plugin Claude uniquement.
Le code serveur MCP n'est pas embarqué ici.

**Conséquence** :
- aucune règle métier fiscale déterministe ne doit être réécrite dans les agents/skills,
- la vérité métier doit provenir des tools MCP appelés via la connexion définie dans `.mcp.json`,
- en absence de MCP, réponse en mode dégradé avec prudence + demande de connexion MCP.
- les appels tools doivent respecter le contrat consommateur défini dans `assets/MCP_CONSUMER_INTERFACE_CONTRACT.md` (noms d'outils, champs requis, format d'erreur).

**Interdit** :
- hardcoder des règles fiscales "techniques" dans un agent,
- simuler un résultat tool comme s'il venait du MCP,
- masquer un statut `human_review` retourné par les tools.

## Vérification rapide

Avant commit :
- vérifier que le frontmatter est valide,
- vérifier que la mission est testable sur un cas simple,
- vérifier que la sortie est compatible avec l'orchestrateur.
