from app.model import Champ

from pydantic import BaseModel

class Annotation(BaseModel):
    type: Champ
    beneficiaire: Champ
    associated_prestation_id: Champ
    simulation_montant: Champ
    simulation_explication: Champ
