from fastapi import APIRouter
from ..utils import logger
from ..catala.aides import impot_revenu

router = APIRouter()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}


@router.get("/aide_scolarite/montant")
def read_aide_scolaire_eligibilite():
    return impot_revenu(1000)

@router.get("/error-simulator")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    division_by_zero = 1 / 0