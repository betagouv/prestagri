from typing import List

from app.model import Annotation, Prestation

from pydantic import BaseModel

class BlurredPrestation(BaseModel):
    id: str
    mois_depot: int
    annee_depot: int
    delai_instruction: int | None
    delai_dernier_changement: int | None
    matricule: str
    affectation: str
    category: str
    civilite: str
    departement:str
    decennie: str
    type: str
    revenu_fiscal: int
    qf_simule: int
    qf_retenu: int
    montant_simule: str
    montant_retenu: str
