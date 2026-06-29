from .generated.catala_runtime import Money as Money_cat, Integer
from .generated.Personne import Personne as Personne_cat
from .generated.Trajet import Trajet as Trajet_cat
from .generated.Menage import Menage as Menage_cat
from ..model import Menage, Personne, Trajet, Centimes
from gmpy2 import mpq

def to_Menage_cat(Menage: Menage) -> Menage_cat:
    membres_cat = to_personne_cat_list(Menage.membres)
    Menage_cat = Menage_cat(
        Menage.personne_ou_enfant_porteur_handicap,
        Menage.garde_alternee,
        Menage.parent_isole,
        Menage.outre_mer,
        membres_cat
    )
    return Menage_cat

def to_personne_cat_list(personnes: list[Personne]) -> list[Personne_cat]:
    return list(map(to_personne_cat, personnes))

def to_personne_cat(personne: Personne) -> Personne_cat:
    return Personne_cat(to_money(personne.revenu), Integer(personne.enfants))

def to_money(centimes: Centimes) -> Money_cat:
    return Money_cat(Integer(centimes.valeur))

def to_trajet(trajet: Trajet) -> Trajet_cat:
    return Trajet_cat(distance_km=Integer(trajet.distance_km),duree_minutes=Integer(trajet.duree_minutes))

def to_float(_mpq: mpq):
    [a, b] = _mpq.as_integer_ratio()
    return float(round(a / b, 5))
