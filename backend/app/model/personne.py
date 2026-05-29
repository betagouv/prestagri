from pydantic import BaseModel

class Personne(BaseModel):
    revenu: int
    enfants: int 