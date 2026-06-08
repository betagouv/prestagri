from .generated.catala_runtime import Money as Money_cat, Integer
from .generated.Personne import Personne as Personne_cat
from .generated.Trajet import Trajet as Trajet_cat
from .generated.Famille import Famille as Famille_cat
from ..model import Famille, Personne, Trajet

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
    return Personne_cat(to_money(personne.revenu*100), Integer(personne.enfants))

def to_money(value: int) -> Money_cat:
    return  Money_cat(Integer(value))

def to_trajet(trajet: Trajet) -> Trajet_cat:
    return Trajet_cat(distance_km=Integer(trajet.distance_km),duree_minutes=Integer(trajet.duree_minutes))