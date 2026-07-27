import sentry_sdk
from fastapi import APIRouter

from app.utils import logger
from app.services.properties import properties

from app.model import Response

router = APIRouter()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}

@router.get("/error-simulator")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        sentry_sdk.capture_exception(e)
        logger.exception(e)
        return Response(value="Une erreur est survenue", explanation=properties.error_contact)
