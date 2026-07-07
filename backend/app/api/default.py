import sentry_sdk
from fastapi import APIRouter

from ..services.properties import Properties
from ..utils import logger
from ..model import Menage, FoyerFiscal, Response, Centimes
from ..services.quotient_familial import get_quotient_familial
from ..services.aide_scolarite import get_aide_scolarite

router = APIRouter()
properties = Properties.import_properties()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}

@router.get("/quotient_familial")
def read_quotient_familial(
    agent_revenu: int,
    agent_enfants: int,
    conjoint_revenu: int | None = None,
    conjoint_enfants: int | None = None,
    beneficiaire_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False
    ) -> Response :
    try : 
        agent = FoyerFiscal(revenu=Centimes.from_euros_int(agent_revenu), personnes=agent_enfants)
        membres = [agent]
        if conjoint_revenu is not None and conjoint_enfants is not None:
            conjoint = FoyerFiscal(revenu=Centimes.from_euros_int(conjoint_revenu), personnes=conjoint_enfants)
            membres.append(conjoint)
        menage = Menage(beneficiaire_porteur_handicap=beneficiaire_porteur_handicap, garde_alternee=garde_alternee, parent_isole=parent_isole, outre_mer=outre_mer, membres=membres)
        response = get_quotient_familial(menage)
        return Response(value=str(response.value), explanation= response.explanation)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.exception(e)
        return Response(value="Une erreur est survenue", explanation=properties.error_contact)

@router.get("/aide_scolarite")
def read_quotient_familial_aide_scolarite(
    agent_revenu: int,
    agent_enfants: int,
    adresse_agent: str,
    adresse_etablissement: str,
    conjoint_revenu: int | None = None,
    conjoint_enfants: int | None = None,
    etudiant_revenu: int  | None = None,
    etudiant_enfants: int | None = None,
    beneficiaire_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False,
    adresse_etudiant: str | None = None,
    montant_materiel_specifique: int | None = None,
    etudiant_post_bac: bool = False,
    ) -> Response:
    try:
        agent = FoyerFiscal(revenu=Centimes.from_euros_int(agent_revenu), personnes=agent_enfants)
        membres = [agent]
        if conjoint_revenu is not None:
            conjoint = FoyerFiscal(revenu=Centimes.from_euros_int(conjoint_revenu), personnes=conjoint_enfants or 0)
            membres.append(conjoint)
        etudiant_independant = FoyerFiscal(revenu=Centimes.from_euros_int(etudiant_revenu), personnes=etudiant_enfants or 0) if etudiant_revenu is not None else None
        menage = Menage(beneficiaire_porteur_handicap=beneficiaire_porteur_handicap, garde_alternee=garde_alternee, parent_isole=parent_isole, outre_mer=outre_mer, membres=membres)
        response = get_aide_scolarite(menage, etudiant_independant,
            adresse_agent, adresse_etablissement, adresse_etudiant,
            Centimes.from_euros_int(montant_materiel_specifique) if montant_materiel_specifique is not None else None,
            etudiant_post_bac)
        return Response(value=str(response.value) , explanation=response.explanation)
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



