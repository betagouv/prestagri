import textwrap
from typing import Any
from datetime import  date

from app.catala.aides import get_catala_aide_handicap_moins_20ans
from app.model import Response

def get_aide_handicap_moins_20ans(annee_demandee: int, date_naissance: date, date_fin_validite: date, pourcentage_incapacite_permanente: int, pourcentage_hors_internat: int) -> Response :
    aide = get_catala_aide_handicap_moins_20ans(annee_demandee=annee_demandee, date_naissance=date_naissance, date_fin_validite=date_fin_validite, pourcentage_incapacite_permanente=pourcentage_incapacite_permanente, pourcentage_hors_internat=pourcentage_hors_internat)
    aide.formatted_explanation = format_explanation(aide.explanation)
    return aide

def format_explanation(raw_explanation: Any) ->  str :

    str_explanation = {
        "alerte_derniere_annee": "oui" if raw_explanation["alerte_derniere_annee"] else "non",
        "versements": [str(v) for v in raw_explanation["versements"]]

    }
    template_explanation = """
        versements : {versements}
        alerte dernière année de versement (car l'enfant aura 20 ans) : {alerte_derniere_annee}
    """

    return textwrap.dedent(template_explanation.format(**str_explanation)).strip()
