from .generated.catala_runtime import Money as Money_cat, Integer, CatalaEnum
from .generated.Foyer_fiscal import FoyerFiscal as Foyer_fiscal_cat
from .generated.Trajet import Trajet as Trajet_cat
from .generated.Menage import Menage as Menage_cat
from ..model import Menage, FoyerFiscal, Trajet, Centimes, centimes
from gmpy2 import mpq

def to_menage_cat(menage: Menage) -> Menage_cat:
    membres_cat = to_personne_cat_list(menage.membres)
    menage_cat = Menage_cat(
        beneficiaire_porteur_handicap=menage.beneficiaire_porteur_handicap,
        garde_alternee=menage.garde_alternee,
        parent_isole=menage.parent_isole,
        outre_mer=menage.outre_mer,
        membres_du_foyer=membres_cat
    )
    return menage_cat

def to_personne_cat_list(personnes: list[FoyerFiscal]) -> list[Foyer_fiscal_cat]:
    return list(map(to_personne_cat, personnes))

def to_personne_cat(personne: FoyerFiscal) -> Foyer_fiscal_cat:
    return Foyer_fiscal_cat(revenu_fiscal_reference=to_money_cat(personne.revenu),
                            nombre_personnes=Integer(personne.personnes))

def to_money_cat(cents: Centimes) -> Money_cat:
    return Money_cat(cents.valeur/100) ## the whole cents setup may seem overengineered now that we end up dividing again but for context the Money used to ask for cents

def to_trajet(trajet: Trajet) -> Trajet_cat:
    return Trajet_cat(distance_km=Integer(trajet.distance_km),duree_minutes=Integer(trajet.duree_minutes))

def to_float(_mpq: mpq):
    [a, b] = _mpq.as_integer_ratio()
    return float(round(a / b, 5))

def cat_enum_to_string(enum: CatalaEnum) -> str :
    return str(enum.code) + " : " + str(enum.payload)
