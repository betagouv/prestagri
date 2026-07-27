import sentry_sdk
from fastapi import APIRouter

from app.services.pilotage import upload_pilotage_data
from app.utils import logger

router = APIRouter()

@router.get("/pilotage")
def read_root():
    logger.info('Pilotage')
    return "piloted"
    #return upload_pilotage_data()
