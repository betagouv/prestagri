from pydantic import BaseModel
from app.model import Foyer_fiscal

class Menage (BaseModel):
    beneficiaire_porteur_handicap: bool
    garde_alternee: bool
    parent_isole: bool
    outre_mer: bool
    membres: list[Foyer_fiscal]