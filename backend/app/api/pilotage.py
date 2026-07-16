import sentry_sdk
from fastapi import APIRouter

from ..services.pilotage import get_dn_dossiers
from ..utils import logger

router = APIRouter()

@router.get("/pilotage")
def read_root():
    logger.info('Pilotage')
    return get_dn_dossiers()
