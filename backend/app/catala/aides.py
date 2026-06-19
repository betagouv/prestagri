
from .generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from .generated.Aide_scolarite import CalculQuotientFamilialAideScolariteIn, calcul_quotient_familial_aide_scolarite, CalculPointsAideScolariteIn, calcul_points_aide_scolarite, calcul_aide_scolarite, CalculAideScolariteIn, Integer
from .generated.catala_runtime import Option
from ..model import Famille, Personne, Trajet, Response, Centimes
from .utils import to_famille_cat, to_personne_cat_list, to_money, to_trajet

def get_catala_quotient_familial(famille : Famille) -> Response[Centimes]:
    famille_cat = to_famille_cat(famille)
    result = calcul_quotient_familial(CalculQuotientFamilialIn(famille_cat))
    return Response (
        value=Centimes(valeur=result.quotient_familial.value.value),
        explanation=str(result.revenu_fiscal_reference) + "/ (12 x " + str(result.nombre_unites) +")"
    )

def get_catala_aide_scolarite(quotient_familial: Centimes, nb_points: int ) -> Response[Centimes]:
    result = calcul_aide_scolarite(CalculAideScolariteIn(to_money(quotient_familial), Integer(nb_points)))
    value = Centimes(valeur=result.aide_scolarite.value.value)
    return Response(
        value=value,
        explanation=str(quotient_familial) + " x " + str(nb_points) + " = " + str(value) )


def get_catala_quotient_familial_aide_scolarite(famille: Famille, etudiants_fiscalement_independants: list[Personne]) -> Response[Centimes]:
    famille_cat = to_famille_cat(famille)
    etudiants_cat = to_personne_cat_list(etudiants_fiscalement_independants)
    result = calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(famille_cat, etudiants_cat))
    value = Centimes(valeur=result.quotient_familial.value.value)
    return Response (
        value=value,
        explanation=str(result.revenu_fiscal_reference) + "/ (12 x " + str(result.nombre_unites) +") = " + str(value)
    )

def get_catala_criteres_eligibles_aide_scolarite(
        trajet_depuis_domicile_agent: Trajet,
        trajet_depuis_domicile_etudiant: None|Trajet,
        montant_materiel_specifique: Centimes,
        valeur_point: Centimes,
        etudiant_en_filiere_post_bac: bool
    ) -> Response[int]:

    optionnel_trajet_depuis_domicile_etudiant = Option(to_trajet(trajet_depuis_domicile_etudiant)) if trajet_depuis_domicile_etudiant is not None else Option(None)
    result = calcul_points_aide_scolarite(
        CalculPointsAideScolariteIn(
            to_trajet(trajet_depuis_domicile_agent),
            optionnel_trajet_depuis_domicile_etudiant,
            to_money(montant_materiel_specifique),
            to_money(valeur_point),
            etudiant_en_filiere_post_bac))
    return Response(value= result.nb_points.value, explanation=str(list(map(str, result.criteres_applicables))))

