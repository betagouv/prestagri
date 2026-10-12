import textwrap
from typing import Any
from datetime import date

from app.catala.aides import get_catala_sejour_loisir_sans_hebergement
from app.services.quotient_familial import get_quotient_familial
from app.model import Response, Centimes, Menage


def get_sejour_loisir_sans_hebergement(
    menage: Menage,
    date_naissance: date,
    date_debut_sejour: date,
    duree_sejour: float,
    montant_debourse: Centimes,
    centre_agree: bool
) -> Response:
    quotient_familial_response = get_quotient_familial(menage)
    aide = get_catala_sejour_loisir_sans_hebergement(
        date_naissance=date_naissance,
        date_debut_sejour=date_debut_sejour,
        duree_sejour=duree_sejour,
        montant_debourse=montant_debourse,
        quotient_familial=quotient_familial_response.value,
        centre_agree=centre_agree
    )
    aide.explanation["quotient_familial"] = quotient_familial_response.value
    aide.formatted_explanation = format_explanation(aide.explanation)
    return aide


def format_explanation(raw_explanation: Any) -> str:
    str_explanation = {
        "quotient_familial": raw_explanation["quotient_familial"],
        "taux_jour": raw_explanation["taux_jour"],
        "taux_demi_jour": raw_explanation["taux_demi_jour"],
        "duree_sejour":  raw_explanation["duree_sejour"],
        "aide": raw_explanation["aide"]
    }
    template_explanation = """
        Quotient Familial : {quotient_familial}
        Taux jour : {taux_jour}
        Taux demi-journée : {taux_demi_jour}
        Durée du séjour : {duree_sejour}
        Aide calculée : {aide}
    """
    return textwrap.dedent(template_explanation.format(**str_explanation)).strip()
