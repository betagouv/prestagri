from pydantic import BaseModel
from app.model import Personne

class Famille (BaseModel):
    personne_ou_enfant_porteur_handicap: bool
    garde_alternee: bool
    parent_isole: bool
    outre_mer: bool
    membres: list[Personne]