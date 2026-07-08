
from .generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from .generated.Aide_scolarite import CalculQuotientFamilialAideScolariteIn, calcul_quotient_familial_aide_scolarite, CalculPointsAideScolariteIn, calcul_points_aide_scolarite, calcul_aide_scolarite, CalculAideScolariteIn, Integer
from .generated.catala_runtime import Option
from ..model import Menage, FoyerFiscal, Trajet, Response, Centimes
from .utils import to_menage_cat, to_personne_cat_list, to_money_cat, to_trajet

def get_catala_quotient_familial(menage : Menage) -> Response[Centimes]:
    menage_cat = to_menage_cat(menage)
    result = calcul_quotient_familial(CalculQuotientFamilialIn(menage_in=menage_cat))
    return Response (
        value=Centimes(valeur=result.quotient_familial),
        explanation= {
            "criteres_applicables" : str(list(map(str, result.criteres_applicables))),
            "calcul" : str(Centimes(valeur=result.revenu_fiscal_reference)) + "/ (12 x (" + str(result.nombre_personnes_vivants_au_foyer) + " + " + str(result.nombre_unites - result.nombre_personnes_vivants_au_foyer) +"))"
        }
    )

def get_catala_aide_scolarite(quotient_familial: Centimes, trajet_depuis_domicile_agent: Trajet,
        trajet_depuis_domicile_etudiant: None|Trajet, montant_materiel_specifique: Centimes,
        valeur_point: Centimes, etudiant_en_filiere_post_bac: bool ) -> Response[Centimes]:

    optionnel_trajet_depuis_domicile_etudiant = Option(to_trajet(trajet_depuis_domicile_etudiant)) if trajet_depuis_domicile_etudiant is not None else Option(None)
    result = calcul_aide_scolarite(CalculAideScolariteIn(
        quotient_familial_in=to_money_cat(quotient_familial),
        trajet_depuis_domicile_agent_in=to_trajet(trajet_depuis_domicile_agent),
        trajet_depuis_domicile_etudiant_in=optionnel_trajet_depuis_domicile_etudiant,
        montant_materiel_specifique_in=to_money_cat(montant_materiel_specifique),
        etudiant_en_filiere_post_bac_in=etudiant_en_filiere_post_bac
    ))
    value = Centimes(valeur=result.aide_scolarite)
    explanation = {
        "critere_applicables": str(list(map(str, result.criteres_applicables))),
        "calcul": str(Centimes(valeur=result.valeur_point)) + " x " + str(result.nb_points) + " = " + str(value)
    }

    return Response(
        value=value,
        explanation= explanation
    )

def get_catala_quotient_familial_aide_scolarite(menage: Menage, etudiants_fiscalement_independants: list[FoyerFiscal]) -> Response[Centimes]:
    menage_cat = to_menage_cat(menage)
    etudiants_cat = to_personne_cat_list(etudiants_fiscalement_independants)
    result = calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(foyer_fiscal_agent_in=menage_cat, etudiants_fiscalement_independants_in=etudiants_cat))
    value = Centimes(valeur=result.quotient_familial)
    return Response (
        value=value,
        explanation= {
            "criteres_applicables": str(list(map(str, result.criteres_applicables))),
            "calcul" :str(Centimes(valeur=result.revenu_fiscal_reference)) + "/ (12 x (" + str(result.nombre_personnes_vivants_au_foyer) + " + " + str(result.nombre_unites - result.nombre_personnes_vivants_au_foyer) +"))"
        }
    )