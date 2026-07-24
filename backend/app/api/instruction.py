import sentry_sdk
from fastapi import APIRouter

from app.services.instruction import upload_dossier_data
from app.utils import logger

router = APIRouter()

@router.get("/instruction/{dossier_number}")
def read_root(dossier_number: str):
    logger.info('instruction ' + dossier_number)
    return upload_dossier_data(dossier_number)
