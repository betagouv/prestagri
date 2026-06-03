from pydantic import BaseModel
from fastapi import APIRouter
from ..utils import logger
from ..catala.aides import quotient_familial, quotient_familial_aide_scolarite
from ..model.famille import Famille
from ..model.personne import Personne


router = APIRouter()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}

class Response(BaseModel):
    value: str
    explanation: str 

@router.get("/quotient_familial")
def read_quotient_familial(
    agent_revenu: int,
    agent_enfants: int,
    conjoint_revenu: int | None = None,
    conjoint_enfants: int | None = None,
    personne_ou_enfant_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False
    ) -> Response :
    famille = create_famille(agent_revenu, agent_enfants, conjoint_revenu, conjoint_enfants, personne_ou_enfant_porteur_handicap, garde_alternee, parent_isole, outre_mer)
    return Response(value = quotient_familial(famille), explanation = "not yet available")


@router.get("/aide_scolarite/quotient_familial")
def read_quotient_familial_aide_scolarite(
    agent_revenu: int,
    agent_enfants: int,
    conjoint_revenu: int | None = None,
    conjoint_enfants: int | None = None,
    etudiant_revenu: int  | None = None,
    etudiant_enfants: int | None = None,
    personne_ou_enfant_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False
    ):
    etudiant_independant = Personne(revenu=etudiant_revenu, enfants=etudiant_enfants)
    famille = create_famille(agent_revenu, agent_enfants, conjoint_revenu, conjoint_enfants, personne_ou_enfant_porteur_handicap, garde_alternee, parent_isole, outre_mer)
    return Response(value = quotient_familial_aide_scolarite(famille, [etudiant_independant]), explanation = "not yet available")

@router.get("/error-simulator")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    division_by_zero = 1 / 0


def create_famille(
    agent_revenu: int,
    agent_enfants: int,
    conjoint_revenu: int | None = None,
    conjoint_enfants: int | None = None,
    personne_ou_enfant_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False) -> Famille :

    membres = [Personne(revenu=agent_revenu, enfants=agent_enfants)]
    if conjoint_revenu != None :
        membres.append(Personne(revenu=conjoint_revenu, enfants=conjoint_enfants|0))
    famille = Famille(
        personne_ou_enfant_porteur_handicap=personne_ou_enfant_porteur_handicap,
        garde_alternee= garde_alternee,
        parent_isole=parent_isole,
        outre_mer=outre_mer,
        membres=membres
    )
    return famille
