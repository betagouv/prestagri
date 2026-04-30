from fastapi import FastAPI
from var import SENTRY_DSN
import sentry_sdk
import logging
logger = logging.getLogger(__name__)

sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    enable_logs=True,
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/sentry-debug")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    division_by_zero = 1 / 0