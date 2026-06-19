from fastapi import APIRouter
from ..utils import logger
from ..model import Famille, Personne, Response, Centimes
from ..services.quotient_familial import get_quotient_familial
from ..services.aide_scolarite import get_aide_scolarite

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
    agent = Personne(revenu=Centimes.from_euros_int(agent_revenu), enfants=agent_enfants)
    membres = [agent]
    if conjoint_revenu is not None:
        conjoint = Personne(revenu=Centimes.from_euros_int(conjoint_revenu), enfants=conjoint_enfants)
        membres.append(conjoint)
    famille = Famille(personne_ou_enfant_porteur_handicap=personne_ou_enfant_porteur_handicap, garde_alternee=garde_alternee, parent_isole=parent_isole, outre_mer=outre_mer, membres=membres)
    response = get_quotient_familial(famille)
    return Response(value=str(response.value), explanation= response.explanation)

@router.get("/aide_scolarite")
def read_quotient_familial_aide_scolarite(
    agent_revenu: int,
    agent_enfants: int,
    adresse_agent: str,
    adresse_etablissement: str,
    conjoint_revenu: int | None = None,
    conjoint_enfants: int | None = None,
    etudiant_revenu: int  | None = None,
    etudiant_enfants: int | None = None,
    personne_ou_enfant_porteur_handicap: bool = False,
    garde_alternee: bool = False,
    parent_isole: bool = False,
    outre_mer: bool = False,
    adresse_etudiant: str | None = None,
    montant_materiel_specifique: int | None = None,
    etudiant_post_bac: bool = False,
    ) -> Response:
    agent = Personne(revenu=Centimes.from_euros_int(agent_revenu), enfants=agent_enfants)
    membres = [agent]
    if conjoint_revenu is not None:
        conjoint = Personne(revenu=Centimes.from_euros_int(conjoint_revenu), enfants=conjoint_enfants)
        membres.append(conjoint)
    etudiant_independant = Personne(revenu=Centimes.from_euros_int(etudiant_revenu), enfants=etudiant_enfants) if etudiant_revenu is not None else None
    famille = Famille(personne_ou_enfant_porteur_handicap=personne_ou_enfant_porteur_handicap, garde_alternee=garde_alternee, parent_isole=parent_isole, outre_mer=outre_mer, membres=membres)
    response = get_aide_scolarite(famille, etudiant_independant,
        adresse_agent, adresse_etablissement, adresse_etudiant,
        montant_materiel_specifique,
        etudiant_post_bac)
    return Response(value=str(response.value) , explanation=response.explanation)


@router.get("/error-simulator")
async def trigger_error():
    logger.info('This will be sent to Sentry')
    division_by_zero = 1 / 0


