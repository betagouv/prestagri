import sentry_sdk
from fastapi import APIRouter

from app.services.instruction import prefill_dossier_annotations
from app.utils import logger

router = APIRouter()

@router.get("/instruction/{dossier_number}")
def read_root(dossier_number: str):
    logger.info('instruction ' + dossier_number)
    prefill_dossier_annotations(dossier_number)
    return "Instruction pré-remplie"
