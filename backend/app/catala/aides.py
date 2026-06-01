
from .generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from .generated.Aide_scolarite import CalculQuotientFamilialAideScolariteIn, calcul_quotient_familial_aide_scolarite
from .generated.catala_runtime import Money, Integer
from .generated.Personne import Personne as Personne_cat
from .generated.Famille import Famille as Famille_cat
from ..model.famille import Famille
from ..model.personne import Personne
from .utils import to_famille_cat, to_personne_cat_list

def quotient_familial(famille : Famille) -> str:
    famille_cat = to_famille_cat(famille)
    return str(calcul_quotient_familial(CalculQuotientFamilialIn(famille_cat)).quotient_familial)

def quotient_familial_aide_scolarite(famille: Famille, etudiants_fiscalement_independants: list[Personne]) -> str: 
    famille_cat = to_famille_cat(famille)
    etudiants_cat = to_personne_cat_list(etudiants_fiscalement_independants)
    return str(calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(famille_cat, etudiants_cat)).quotient_familial)
