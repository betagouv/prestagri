from pydantic import BaseModel
from datetime import date

from app.model import Centimes


class Versement(BaseModel):
    date: date
    montant: Centimes

    def __str__(self) -> str :
        return str(self.montant) + " à verser le " + self.date.isoformat()
