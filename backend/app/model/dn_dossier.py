from datetime import datetime
from enum import Enum
from typing import List

from app.model import Annotation, Prestation

from pydantic import BaseModel

class DossierState(Enum):
    CONSTRUCTION = "en_construction"
    INSTRUCTION = "en_instruction"
    ACCEPTE = "accepte"
    REFUSE = "refuse"
    SANS_SUITE = "sans_suite"

class DNDossier(BaseModel):
    id: str
    state: DossierState
    date_depot: datetime
    date_instruction: datetime | None
    date_dernier_changement: datetime
    matricule: str
    affectation: str
    category: str
    civilite: str
    adresse: str
    revenu_fiscal_reference: str
    date_naissance: str
    prestations: List[Prestation]
    annotations: List[Annotation]
