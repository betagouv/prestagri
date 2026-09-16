from datetime import date

from app.catala.generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from app.catala.generated.Handicap_moins_20_ans import CalculAideHandicapMoins20AnsIn, calcul_aide_handicap_moins20_ans
from app.catala.generated.Aide_scolarite import CalculQuotientFamilialAideScolariteIn, calcul_quotient_familial_aide_scolarite, CalculPointsAideScolariteIn, calcul_points_aide_scolarite, calcul_aide_scolarite, CalculAideScolariteIn, Integer
from app.catala.generated.catala_runtime import Option
from app.model import Menage, FoyerFiscal, Trajet, Response, Centimes
from app.catala.utils import to_menage_cat, to_personne_cat_list, to_money_cat, to_trajet_cat, cat_enum_to_string, to_date_cat, from_date_cat, from_versement_cat

def get_catala_quotient_familial(menage : Menage) -> Response[Centimes]:
    menage_cat = to_menage_cat(menage)
    result = calcul_quotient_familial(CalculQuotientFamilialIn(menage_in=menage_cat))
    return Response (
        value=Centimes(valeur=result.quotient_familial),
        explanation= {
            "critères_applicables" : str(list(map(cat_enum_to_string, result.criteres_applicables))),
            "calcul" : str(Centimes(valeur=result.revenu_fiscal_reference)) + "/ (12 x (" + str(result.nombre_personnes_vivants_au_foyer) + " + " + str(result.nombre_unites - result.nombre_personnes_vivants_au_foyer) +"))"
        }
    )

def get_catala_aide_scolarite(menage: Menage, etudiants_fiscalement_independants: list[FoyerFiscal], trajet_depuis_domicile_agent: Trajet,
        trajet_depuis_domicile_etudiant: None|Trajet, montant_materiel_specifique: Centimes,
        etudiant_en_filiere_post_bac: bool ) -> Response[Centimes]:

    optionnel_trajet_depuis_domicile_etudiant = Option(to_trajet_cat(trajet_depuis_domicile_etudiant)) if trajet_depuis_domicile_etudiant is not None else Option(None)
    result = calcul_aide_scolarite(CalculAideScolariteIn(
        menage_agent_in= to_menage_cat(menage),
        etudiants_fiscalement_independants_in=to_personne_cat_list(etudiants_fiscalement_independants),
        trajet_depuis_domicile_agent_in=to_trajet_cat(trajet_depuis_domicile_agent),
        trajet_depuis_domicile_etudiant_in=optionnel_trajet_depuis_domicile_etudiant,
        montant_materiel_specifique_in=to_money_cat(montant_materiel_specifique),
        etudiant_en_filiere_post_bac_in=etudiant_en_filiere_post_bac
    ))
    value = Centimes(valeur=result.aide_scolarite)
    raw_explanation = {
        "critères_applicables_quotient_familial": str(list(map(cat_enum_to_string, result.criteres_applicables_quotient_familial))),
        "calcul_quotient_familial": str(Centimes(valeur=result.revenu_fiscal_reference)) + "/ (12 x (" + str(
            result.nombre_personnes_vivants_au_foyer) + " + " + str(
            result.nombre_unites - result.nombre_personnes_vivants_au_foyer) + "))",
        "quotient_familial": float(Centimes(valeur=result.quotient_familial)),
        "revenu_fiscal_reference": float(Centimes(valeur=result.revenu_fiscal_reference)),
        "critères_applicables_aide_scolarité": str(list(map(cat_enum_to_string, result.criteres_applicables))),
        "valeur_point": str(Centimes(valeur=result.valeur_point)),
        "calcul_aide_scolarité": str(Centimes(valeur=result.valeur_point)) + " x " + str(result.nb_points) + " = " + str(value)
    }


    return Response(
        value=value,
        explanation= raw_explanation
    )

def get_catala_quotient_familial_aide_scolarite(menage: Menage, etudiants_fiscalement_independants: list[FoyerFiscal]) -> Response[Centimes]:
    menage_cat = to_menage_cat(menage)
    etudiants_cat = to_personne_cat_list(etudiants_fiscalement_independants)
    result = calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(menage_agent_in=menage_cat, etudiants_fiscalement_independants_in=etudiants_cat))
    value = Centimes(valeur=result.quotient_familial)
    return Response (
        value=value,
        explanation= {
            "critères_applicables": str(list(map(cat_enum_to_string, result.criteres_applicables))),
            "calcul" :str(Centimes(valeur=result.revenu_fiscal_reference)) + "/ (12 x (" + str(result.nombre_personnes_vivants_au_foyer) + " + " + str(result.nombre_unites - result.nombre_personnes_vivants_au_foyer) +"))"
        }
    )

def get_catala_aide_handicap_moins_20ans(annee_demandee: int, date_naissance: date, date_fin_validite: date, pourcentage_incapacite_permanente: int, pourcentage_hors_internat: int) -> Response[Centimes]:
    result = calcul_aide_handicap_moins20_ans(
        CalculAideHandicapMoins20AnsIn(
            annee_demandee_in= Integer(annee_demandee),
            date_naissance_enfant_in= to_date_cat(date_naissance),
            date_fin_validite_AEEH_in= to_date_cat(date_fin_validite),
            pourcentage_incapacite_permanente_in= Integer(pourcentage_incapacite_permanente),
            pourcentage_temps_hors_internat_avec_prise_en_charge_in= Integer(pourcentage_hors_internat)
        )
    )
    value = Centimes(valeur=result.aide_handicap)
    return Response (
        value= value,
        explanation= {
            "versements": [from_versement_cat(v) for v in result.versements],
            "alerte_derniere_annee": bool(result.alerte_derniere_annee.value)
        }
    )
