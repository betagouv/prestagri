
from .generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from .generated.Aide_scolarite import CalculQuotientFamilialAideScolariteIn, calcul_quotient_familial_aide_scolarite, CalculPointsAideScolariteIn, calcul_points_aide_scolarite, calcul_aide_scolarite, CalculAideScolariteIn, Integer
from .generated.catala_runtime import Option, Decimal
from ..model import Menage, Personne, Trajet, Response, Centimes
from .utils import to_Menage_cat, to_personne_cat_list, to_money, to_trajet, to_float


def get_catala_quotient_familial(Menage : Menage) -> Response[Centimes]:
    Menage_cat = to_Menage_cat(Menage)
    result = calcul_quotient_familial(CalculQuotientFamilialIn(Menage_cat))
    return Response (
        value=Centimes(valeur=result.quotient_familial.value.value),
        explanation=str(result.revenu_fiscal_reference) + "/ (12 x " + str(result.nombre_unites) +")"
    )

def get_catala_aide_scolarite(quotient_familial: Centimes, nb_points: float ) -> Response[Centimes]:
    result = calcul_aide_scolarite(CalculAideScolariteIn(to_money(quotient_familial), Decimal(nb_points)))
    value = Centimes(valeur=result.aide_scolarite.value.value)
    return Response(
        value=value,
        explanation=str(quotient_familial) + " x " + str(nb_points) + " = " + str(value) )


def get_catala_quotient_familial_aide_scolarite(Menage: Menage, etudiants_fiscalement_independants: list[Personne]) -> Response[Centimes]:
    Menage_cat = to_Menage_cat(Menage)
    etudiants_cat = to_personne_cat_list(etudiants_fiscalement_independants)
    result = calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(Menage_cat, etudiants_cat))
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
    ) -> Response[float]:

    optionnel_trajet_depuis_domicile_etudiant = Option(to_trajet(trajet_depuis_domicile_etudiant)) if trajet_depuis_domicile_etudiant is not None else Option(None)
    result = calcul_points_aide_scolarite(
        CalculPointsAideScolariteIn(
            to_trajet(trajet_depuis_domicile_agent),
            optionnel_trajet_depuis_domicile_etudiant,
            to_money(montant_materiel_specifique),
            to_money(valeur_point),
            etudiant_en_filiere_post_bac))
    return Response(value= to_float(result.nb_points.value), explanation=str(list(map(str, result.criteres_applicables))))

