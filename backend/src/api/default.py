from fastapi import APIRouter
from ..utils import logger

router = APIRouter()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@router.get("/sentry-debug")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    division_by_zero = 1 / 0