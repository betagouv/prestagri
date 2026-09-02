from typing import List

from app.model import Annotation, Prestation

from pydantic import BaseModel

class BlurredPrestation(BaseModel):
    id: str
    matricule: str
    affectation: str
    genre: str
    decennie: str
    type: str
    montant_simule: str
