from fastapi import APIRouter
from ..utils import logger

router = APIRouter()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}


@router.get("/aide_scolarite/eligibilite")
def read_aide_scolaire_eligibilite(nb_enfants: int, region: str):
    return True

@router.get("/error-simulator")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    division_by_zero = 1 / 0