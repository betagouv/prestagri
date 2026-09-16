from datetime import date
from .generated.catala_runtime import Money as Money_cat, Integer, CatalaEnum, Date as Date_cat
from .generated.Foyer_fiscal import FoyerFiscal as Foyer_fiscal_cat
from .generated.Trajet import Trajet as Trajet_cat
from .generated.Menage import Menage as Menage_cat
from .generated.Versement import Versement as Versement_cat
from app.model import Menage, FoyerFiscal, Trajet, Centimes, Versement
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

def from_money_cat(money: Money_cat) -> Centimes:
    return Centimes(valeur=int(money))

def to_trajet_cat(trajet: Trajet) -> Trajet_cat:
    return Trajet_cat(distance_km=Integer(trajet.distance_km),duree_minutes=Integer(trajet.duree_minutes))

def to_float(_mpq: mpq):
    [a, b] = _mpq.as_integer_ratio()
    return float(round(a / b, 5))

def cat_enum_to_string(enum: CatalaEnum) -> str :
    return str(enum.code) + " : " + str(enum.payload)

def to_date_cat(date_py: date) -> Date_cat:
    return Date_cat(date_py.year, date_py.month, date_py.day)

def from_date_cat(date_cat: Date_cat) -> date:
    return date(year=date_cat.value.year, month=date_cat.value.month, day=date_cat.value.day)

def from_versement_cat(versement_cat: Versement_cat) -> Versement:
    return Versement(
        montant=from_money_cat(versement_cat.montant),
        date=from_date_cat(versement_cat.date_versement)
    )
