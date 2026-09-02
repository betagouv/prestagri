from app.model import Champ, emptyChamp

from pydantic import BaseModel

class Annotation(BaseModel):
    type: Champ
    beneficiaire: Champ
    associated_prestation_id: Champ
    simulation_montant: Champ
    simulation_explication: Champ

emptyAnnotation = Annotation(
    type=emptyChamp,
    beneficiaire=emptyChamp,
    associated_prestation_id=emptyChamp,
    simulation_montant=emptyChamp,
    simulation_explication=emptyChamp
)
