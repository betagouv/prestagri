
from .generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from .generated.Aide_scolarite import CalculQuotientFamilialAideScolariteIn, calcul_quotient_familial_aide_scolarite, CalculPointsAideScolariteIn, calcul_points_aide_scolarite
from .generated.catala_runtime import Option
from ..model import Famille, Personne, Trajet, Response
from .utils import to_famille_cat, to_personne_cat_list, to_money, to_trajet

def quotient_familial(famille : Famille) -> Response:
    famille_cat = to_famille_cat(famille)
    result = calcul_quotient_familial(CalculQuotientFamilialIn(famille_cat))
    return Response (value=str(result.quotient_familial.value), explanation="a venir")


def quotient_familial_aide_scolarite(famille: Famille, etudiants_fiscalement_independants: list[Personne]) -> Response:
    famille_cat = to_famille_cat(famille)
    etudiants_cat = to_personne_cat_list(etudiants_fiscalement_independants)
    result = calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(famille_cat, etudiants_cat))
    return Response (value=str(result.quotient_familial.value), explanation="a venir")

def criteres_eligibles_aide_scolarite(
        trajet_depuis_domicile_agent: Trajet,
        trajet_depuis_domicile_etudiant: None|Trajet,
        montant_materiel_specifique: int,
        valeur_point:int,
        etudiant_en_filiere_post_bac: bool
    ) -> Response:

    optionnel_trajet_depuis_domicile_etudiant = Option(to_trajet(trajet_depuis_domicile_etudiant)) if trajet_depuis_domicile_etudiant is not None else Option(None)
    result = calcul_points_aide_scolarite(
        CalculPointsAideScolariteIn(
            to_trajet(trajet_depuis_domicile_agent),
            optionnel_trajet_depuis_domicile_etudiant,
            to_money(montant_materiel_specifique),
            to_money(valeur_point),
            etudiant_en_filiere_post_bac))
    return Response(value= str(result.nb_points.value), explanation=str(list(map(str, result.criteres_applicables))))

