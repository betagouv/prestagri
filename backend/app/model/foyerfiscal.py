from pydantic import BaseModel

from app.model import Centimes

class FoyerFiscal(BaseModel):
    revenu: Centimes
    personnes: int
