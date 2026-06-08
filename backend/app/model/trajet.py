from pydantic import BaseModel

class Trajet(BaseModel):
    distance_km: int
    duree_minutes: int