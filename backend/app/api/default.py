from pydantic import BaseModel
from fastapi import APIRouter
from ..utils import logger
from ..catala.aides import quotient_familial, quotient_familial_aide_scolarite, criteres_eligibles_aide_scolarite
from ..model import Famille, Personne, Trajet, Response
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

@router.get("/")
def read_root():
    logger.info('Bienvenu')
    return {"Quelle belle journee pour les abeilles"}

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
    return quotient_familial(famille)


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
    ) -> Response:
    etudiant_independant = Personne(revenu=etudiant_revenu, enfants=etudiant_enfants)
    famille = create_famille(agent_revenu, agent_enfants, conjoint_revenu, conjoint_enfants, personne_ou_enfant_porteur_handicap, garde_alternee, parent_isole, outre_mer)
    return quotient_familial_aide_scolarite(famille, [etudiant_independant])

@router.get("/aide_scolarite/points")
def read_quotient_familial_aide_scolarite(
    adresse_agent: str,
    adresse_etablissement: str,
    adresse_etudiant: str | None = None,
    montant_materiel_specifique: int | None = None,
    etudiant_post_bac: bool = False,
    ) -> Response :
    trajet_agent = Trajet(distance_km=40, duree_minutes=40)
    trajet_etudiant = Trajet(distance_km=30, duree_minutes=30)
    valeur_point = 30
    return criteres_eligibles_aide_scolarite(trajet_agent, trajet_etudiant, montant_materiel_specifique, valeur_point, etudiant_post_bac)


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
