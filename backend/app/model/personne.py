from pydantic import BaseModel

from app.model import Centimes


class Personne(BaseModel):
    revenu: Centimes
    enfants: int 