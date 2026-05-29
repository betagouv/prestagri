from fastapi import APIRouter
from ..utils import logger
from ..catala.aides import impot_revenu, quotient_familial
from ..model.famille import Famille
from ..model.personne import Personne


router = APIRouter()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}


@router.get("/aide_scolarite/montant")
def read_aide_scolaire_eligibilite():
    return impot_revenu(1000)

@router.get("/quotient_familial")
def read_quotient_familial(
    agent_revenu: int,
    agent_enfants: int,
    conjoint_revenu: int,
    conjoint_enfants: int,
    personne_ou_enfant_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False
    ):
    famille = Famille(
        personne_ou_enfant_porteur_handicap= personne_ou_enfant_porteur_handicap,
        garde_alternee= garde_alternee,
        parent_isole=parent_isole,
        outre_mer=outre_mer,
        membres=[
            Personne(revenu=agent_revenu, enfants=agent_enfants),
            Personne(revenu=conjoint_revenu, enfants=conjoint_enfants)
        ]
    )
    return quotient_familial(famille)

@router.get("/error-simulator")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    division_by_zero = 1 / 0