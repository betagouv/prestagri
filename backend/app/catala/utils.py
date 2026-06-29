from .generated.catala_runtime import Money as Money_cat, Integer
from .generated.Foyer_fiscal import FoyerFiscal as Foyer_fiscal_cat
from .generated.Trajet import Trajet as Trajet_cat
from .generated.Menage import Menage as Menage_cat
from ..model import Menage, FoyerFiscal, Trajet, Centimes
from gmpy2 import mpq

def to_menage_cat(menage: Menage) -> Menage_cat:
    membres_cat = to_personne_cat_list(menage.membres)
    menage_cat = Menage_cat(
        menage.beneficiaire_porteur_handicap,
        menage.garde_alternee,
        menage.parent_isole,
        menage.outre_mer,
        membres_cat
    )
    return menage_cat

def to_personne_cat_list(personnes: list[FoyerFiscal]) -> list[Foyer_fiscal_cat]:
    return list(map(to_personne_cat, personnes))

def to_personne_cat(personne: FoyerFiscal) -> Foyer_fiscal_cat:
    return Foyer_fiscal_cat(to_money(personne.revenu), Integer(personne.personnes))

def to_money(centimes: Centimes) -> Money_cat:
    return Money_cat(Integer(centimes.valeur))

def to_trajet(trajet: Trajet) -> Trajet_cat:
    return Trajet_cat(distance_km=Integer(trajet.distance_km),duree_minutes=Integer(trajet.duree_minutes))

def to_float(_mpq: mpq):
    [a, b] = _mpq.as_integer_ratio()
    return float(round(a / b, 5))
