---
title: Mon Service Sécurisé
---

Prest'Agri est référence sur "[Mon Service Sécurisé](https://monservicesecurise.cyber.gouv.fr/service/c33f3974-e893-45b0-9e40-c9e9ce5a8546)"

### Liste des services et données à protéger

Prest'Agri se décompose en 3 facettes :
- Démarches Numérique, stocke l'ensemble des données personnelles
- prest-agri.beta.gouv.fr accéde aux données de DN, les transforme et les transmet à Grist. Aucune donnée n'est stockée. Les clefs servant à l'identification sont stockées dans des variables d'environnemnets sur Scalingo
- Grist, stocke les données liées au pilotage. Toute les données sont anonymisées et celle qui le peuvent sont floutées (arrondie à la décennie, à la centaine d'euros )

### Liste des équipements et des applicatifs contribuant au fonctionnement du système d'information

- Démarches Numériques
- Grist
- Scalingo

### Lister les prestataires et fournisseurs avec leurs coordonnées

- Scalingo
- PathTech (attributaires sous-traitant à Erica Delagnier)
- ?  (attributaires sous-traitant à Amandine Guegano)

### Mécanisme d'audit automatique :
- mise en place de [talisman](https://github.com/thoughtworks/talisman) et pre-commit
- [codeQL](https://codeql.github.com/)

### Formaliser et mettre en œuvre un processus de gestion des arrivées, départs et changements de fonction
