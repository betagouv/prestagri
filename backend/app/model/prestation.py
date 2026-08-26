from pydantic import BaseModel
from typing import Any

class Prestation(BaseModel):
    id: str
    type: str
    enfant: str
    calcul_data: Any
