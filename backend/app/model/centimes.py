from pydantic import BaseModel

class Centimes(BaseModel):
    valeur: int

    def __init__(self, centimes: int):
        self.valeur = centimes

    def to_euros(self) -> str :
        return str(self.valeur/100) + "€"

    @classmethod
    def from_euros(cls, euros: str):
        euros_float = float(euros)
        centimes = int(euros_float * 100)
        return cls(centimes)