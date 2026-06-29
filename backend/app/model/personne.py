from pydantic import BaseModel

from app.model import Centimes

class Foyer_fiscal(BaseModel):
    revenu: Centimes
    enfants: int