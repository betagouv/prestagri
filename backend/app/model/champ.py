from pydantic import BaseModel

class Champ(BaseModel):
    id: str
    value: str
