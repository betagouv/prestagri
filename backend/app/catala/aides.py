from .generated.Personne import Personne as Personne_cat
from .generated.Famille import Famille as Famille_cat
from .generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from .generated.catala_runtime import Money, Integer
from ..model.famille import Famille


def impot_revenu(montant) -> str:
    personne = Personne(Money(Integer(100000)), Integer(3))
    return str(personne)

def quotient_familial(famille) -> str:
    membres_cat = []
    for membre in famille.membres:
        membres_cat += Personne_cat(Money(Integer(membre.revenu*100)), Integer(membre.enfants)),
    famille_cat = Famille_cat(
        famille.personne_ou_enfant_porteur_handicap,
        famille.garde_alternee,
        famille.parent_isole,
        famille.outre_mer,
        membres_cat
    )
    return str(calcul_quotient_familial(CalculQuotientFamilialIn(famille_cat)))