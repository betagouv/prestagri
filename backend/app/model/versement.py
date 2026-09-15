from pydantic import BaseModel
from datetime import date

from app.model import Centimes


class Versement(BaseModel):
    date: date
    montant: Centimes
