# Checklist de soumission - fiscal-fr

## Package

- [x] Dossier de publication separe de l'existant Claude.
- [x] Manifeste Codex present : `codex/plugin/.codex-plugin/plugin.json`.
- [x] Marketplace local de publication present : `.agents/plugins/marketplace.json`.
- [x] Skill autonome present : `codex/plugin/skills/fiscal-fr/SKILL.md`.
- [x] Reference embarquee presente : `codex/plugin/skills/fiscal-fr/REFERENCE.md`.
- [x] Icone presente : `codex/plugin/icon.png`.

## Securite

- [x] Aucun token dans le package.
- [x] Aucun placeholder de jeton d'authentification dans le package.
- [x] MCP declare en OAuth2.
- [x] Logique fiscale deterministe non dupliquee dans du code local.

## Documentation

- [x] README Codex present.
- [x] Politique de confidentialite presente.
- [x] Conditions d'utilisation presentes.
- [x] Changelog present.
- [ ] URLs privacy/TOS a confirmer apres publication du repo public.
- [ ] Screenshots marketplace a ajouter si le canal de soumission les exige.

## Produit fiscal

- [x] Disclaimer fiscal present dans le skill.
- [x] Cas complexes diriges vers revue humaine.
- [x] Points a confirmer exposes a l'utilisateur.
- [ ] Dates de cloture declaration 2026 a confirmer sur impots.gouv.fr.
- [ ] Plafond PER 2025 a confirmer lors de la mise a jour annuelle.

## Validation finale

- [ ] Tester l'installation via le lien Codex du marketplace de publication.
- [ ] Tester la connexion OAuth2 dans l'IHM Codex.
- [ ] Tester au moins un appel MCP `qualify_tax_profile`.
- [ ] Tester un parcours complet : qualification -> justificatifs -> vigilance.
- [ ] Confirmer le canal officiel de soumission Codex Store.
