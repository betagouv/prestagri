from typing import Any, List

from app.model import Annotation, Prestation

from pydantic import BaseModel

class DNDossier(BaseModel):
    id: str
    prestations: List[Prestation]
    annotations: List[Annotation]
    raw: Any
