from pydantic import BaseModel


class Centimes(BaseModel):
    valeur: int

    def __str__(self) -> str :
        return str(self.valeur/100) + "€"

    @classmethod
    def from_euros_int(cls, euros: int):
        centimes = int(euros * 100)
        return cls(valeur=centimes)
