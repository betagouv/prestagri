import sentry_sdk
from fastapi import APIRouter

from ..services.pilotage import upload_pilotage_data
from ..utils import logger

router = APIRouter()

@router.get("/pilotage")
def read_root():
    logger.info('Pilotage')
    return upload_pilotage_data()
