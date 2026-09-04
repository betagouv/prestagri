import sentry_sdk
from fastapi import APIRouter

from app.services.gps import get_trajet
from app.services.properties import properties
from app.utils import logger
from app.model import Menage, FoyerFiscal, Response, Centimes, Trajet
from app.services.quotient_familial import get_quotient_familial
from app.services.aide_scolarite import get_aide_scolarite, format_explanation

router = APIRouter()

@router.get("/quotient_familial")
def read_quotient_familial(
    foyer_fiscal_agent_revenu: int,
    foyer_fiscal_agent_membres: int,
    foyer_fiscal_conjoint_revenu: int | None = None,
    foyer_fiscal_conjoint_membres: int | None = None,
    foyer_fiscal_etudiant_revenu: int | None = None,
    foyer_fiscal_etudiant_membres: int | None = None,
    beneficiaire_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False
    ) -> Response :
    try :
        menage = Menage.create_menage(foyer_fiscal_agent_revenu, foyer_fiscal_agent_membres,
            foyer_fiscal_conjoint_revenu, foyer_fiscal_conjoint_membres,
            foyer_fiscal_etudiant_revenu, foyer_fiscal_etudiant_membres,
            beneficiaire_porteur_handicap, garde_alternee, parent_isole, outre_mer)

        response = get_quotient_familial(menage)
        return Response(value=str(response.value), explanation= response.explanation)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.exception(e)
        return Response(value="Une erreur est survenue", explanation=properties.error_contact)

@router.get("/aide_scolarite/adresse")
def read_quotient_familial_aide_scolarite(
    foyer_fiscal_agent_revenu: int,
    foyer_fiscal_agent_membres: int,
    adresse_agent: str,
    adresse_etablissement: str,
    foyer_fiscal_conjoint_revenu: int | None = None,
    foyer_fiscal_conjoint_membres: int | None = None,
    foyer_fiscal_etudiant_revenu: int | None = None,
    foyer_fiscal_etudiant_membres: int | None = None,
    beneficiaire_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False,
    adresse_etudiant: str | None = None,
    montant_materiel_specifique: int | None = None,
    etudiant_post_bac: bool = False,
    ) -> Response:
    try:
        menage = Menage.create_menage(foyer_fiscal_agent_revenu, foyer_fiscal_agent_membres,
                                      foyer_fiscal_conjoint_revenu, foyer_fiscal_conjoint_membres,
                                      None, None,
                                      beneficiaire_porteur_handicap, garde_alternee, parent_isole, outre_mer)
        etudiant_independant = FoyerFiscal(revenu=Centimes.from_euros_int(foyer_fiscal_etudiant_revenu), personnes=foyer_fiscal_etudiant_membres or 0) if foyer_fiscal_etudiant_revenu is not None else None
        trajet_etudiant =  get_trajet(adresse_depart=adresse_etudiant, adresse_arrivee=adresse_etablissement)  if (adresse_etudiant is not None ) else None
        trajet_agent = get_trajet(adresse_depart=adresse_agent, adresse_arrivee=adresse_etablissement)
        montant_materiel = Centimes.from_euros_int(montant_materiel_specifique) if montant_materiel_specifique is not None else None

        response = get_aide_scolarite(menage, etudiant_independant, trajet_agent, trajet_etudiant ,montant_materiel,etudiant_post_bac)
        return Response(value=str(response.value) , explanation=response.explanation)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.exception(e)
        return Response(value="Une erreur est survenue", explanation=properties.error_contact)

@router.get("/aide_scolarite/trajet")
def read_quotient_familial_aide_scolarite(
    foyer_fiscal_agent_revenu: int,
    foyer_fiscal_agent_membres: int,
    trajet_agent_km: int,
    trajet_agent_min: int,
    foyer_fiscal_conjoint_revenu: int | None = None,
    foyer_fiscal_conjoint_membres: int | None = None,
    foyer_fiscal_etudiant_revenu: int | None = None,
    foyer_fiscal_etudiant_membres: int | None = None,
    beneficiaire_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False,
    trajet_etudiant_km: int | None = None,
    trajet_etudiant_min: int | None = None,
    montant_materiel_specifique: int | None = None,
    etudiant_post_bac: bool = False,
    ) -> Response:
    try:
        menage = Menage.create_menage(foyer_fiscal_agent_revenu, foyer_fiscal_agent_membres,
                                      foyer_fiscal_conjoint_revenu, foyer_fiscal_conjoint_membres,
                                      None, None,
                                      beneficiaire_porteur_handicap, garde_alternee, parent_isole, outre_mer)
        etudiant_independant = FoyerFiscal(revenu=Centimes.from_euros_int(foyer_fiscal_etudiant_revenu), personnes=foyer_fiscal_etudiant_membres or 0) if foyer_fiscal_etudiant_revenu is not None else None
        trajet_etudiant = Trajet(distance_km=trajet_etudiant_km, duree_minutes=trajet_etudiant_min) if (trajet_etudiant_km is not None and trajet_etudiant_min is not None) else None
        trajet_agent = Trajet(distance_km=trajet_agent_km, duree_minutes=trajet_agent_min)
        montant_materiel = Centimes.from_euros_int(montant_materiel_specifique) if montant_materiel_specifique is not None else None

        response = get_aide_scolarite(menage, etudiant_independant, trajet_agent, trajet_etudiant ,montant_materiel,etudiant_post_bac)
        return Response(value=str(response.value) , explanation=format_explanation(response.explanation))
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.exception(e)
        return Response(value="Une erreur est survenue", explanation=properties.error_contact)



@router.get("/error-simulator")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.exception(e)
        return Response(value="Une erreur est survenue", explanation=properties.error_contact)
