from typing import List

from app.model import Annotation, Prestation

from pydantic import BaseModel

class DNDossier(BaseModel):
    id: str
    matricule: str
    affectation: str
    securite_sociale: str
    adresse: str
    date_naissance: str
    prestations: List[Prestation]
    annotations: List[Annotation]
