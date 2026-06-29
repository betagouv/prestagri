from pydantic import BaseModel
from app.model import FoyerFiscal

class Menage (BaseModel):
    personne_ou_enfant_porteur_handicap: bool
    garde_alternee: bool
    parent_isole: bool
    outre_mer: bool
    membres: list[FoyerFiscal]