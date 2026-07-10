from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from .config import setup_sentry
from .api import calculatrice
from .api import pilotage
from fastapi.middleware.cors import CORSMiddleware

setup_sentry()
app = FastAPI()
origins = [
    "*",
    "https://doc.prest-agri.beta.gouv.fr/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculatrice.router)
app.include_router(pilotage.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Prest'Agri",
        version="0.0.1",
        summary="Api mise a disposition pour Demarche Numerique",
        description="",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi