from .generated.catala_runtime import Money as Money_cat, Integer
from .generated.Foyer_fiscal import Foyer_fiscal as Foyer_fiscal_cat
from .generated.Trajet import Trajet as Trajet_cat
from .generated.Menage import Menage as Menage_cat
from ..model import Menage, Foyer_fiscal, Trajet, Centimes
from gmpy2 import mpq

def to_Menage_cat(Menage: Menage) -> Menage_cat:
    membres_cat = to_foyer_fiscal_cat_list(Menage.membres)
    Menage_cat = Menage_cat(
        Menage.beneficiaire_porteur_handicap,
        Menage.garde_alternee,
        Menage.parent_isole,
        Menage.outre_mer,
        membres_cat
    )
    return Menage_cat

def to_foyer_fiscal_cat_list(foyer_fiscals: list[Foyer_fiscal]) -> list[Foyer_fiscal_cat]:
    return list(map(to_foyer_fiscal_cat, foyer_fiscals))

def to_foyer_fiscal_cat(foyer_fiscal: Foyer_fiscal) -> Foyer_fiscal_cat:
    return Foyer_fiscal_cat(to_money(foyer_fiscal.revenu), Integer(foyer_fiscal.enfants))

def to_money(centimes: Centimes) -> Money_cat:
    return Money_cat(Integer(centimes.valeur))

def to_trajet(trajet: Trajet) -> Trajet_cat:
    return Trajet_cat(distance_km=Integer(trajet.distance_km),duree_minutes=Integer(trajet.duree_minutes))

def to_float(_mpq: mpq):
    [a, b] = _mpq.as_integer_ratio()
    return float(round(a / b, 5))
