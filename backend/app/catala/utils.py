from .generated.catala_runtime import Money, Integer
from .generated.Personne import Personne as Personne_cat
from .generated.Famille import Famille as Famille_cat
from ..model.famille import Famille
from ..model.personne import Personne

def to_famille_cat(famille: Famille) -> Famille_cat: 
    membres_cat = to_personne_cat_list(famille.membres)
    famille_cat = Famille_cat(
        famille.personne_ou_enfant_porteur_handicap,
        famille.garde_alternee,
        famille.parent_isole,
        famille.outre_mer,
        membres_cat
    )
    return famille_cat

def to_personne_cat_list(personnes: list[Personne]) -> list[Personne_cat]:
    return list(map(to_personne_cat, personnes))

def to_personne_cat(personne: Personne) -> Personne_cat:
    return Personne_cat(Money(Integer(personne.revenu*100)), Integer(personne.enfants))