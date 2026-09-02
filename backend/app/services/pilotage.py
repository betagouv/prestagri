import requests
import json
from typing import Any, List

from app.services.properties import properties
from app.services.demarche_numerique import get_pilotage_data
from app.services.blurring import blur_birthdate, blur_id
from app.model import DNDossier, BlurredPrestation, Prestation, Annotation, emptyAnnotation


def upload_pilotage_data() -> Any:
    dn_dossiers = get_pilotage_data()
    blurred_prestations = blur_all_prestations(dn_dossiers)
    uploaded = send_data_to_grist(blurred_prestations)
    return {
        "dn": dn_dossiers,
        "blurred": blurred_prestations,
        "uploaded": uploaded
    }

def blur_all_prestations(dn_dossiers: List[DNDossier]) -> List[BlurredPrestation]:
    blurred_prestations = []
    for dossier in dn_dossiers :
        prestations = get_prestations(dossier)
        blurred_prestations += prestations
    return blurred_prestations

def get_prestations(dn_dossier: DNDossier) -> List[BlurredPrestation]:
    blurred = []
    for prestation in dn_dossier.prestations:
        annotation = get_annotation(prestation, dn_dossier)
        blurred.append(
            BlurredPrestation(
                id= blur_id(prestation.id),
                matricule=blur_id(dn_dossier.matricule),
                affectation=dn_dossier.affectation,
                genre=dn_dossier.genre,
                decennie=blur_birthdate(dn_dossier.date_naissance),
                type= prestation.type,
                montant_simule=annotation.simulation_montant.value
            )
        )
    return blurred

def get_annotation(prestation: Prestation, dossier: DNDossier) -> Annotation:
    for annotation in dossier.annotations:
        if annotation.associated_prestation_id.value == prestation.id:
            return annotation
    return emptyAnnotation

def send_data_to_grist(prestations: List[BlurredPrestation]) -> Any :
    if len(prestations) < 1 :
        return {"explanation": "no data to upload"}
    url = "https://grist.numerique.gouv.fr/api/docs/"+properties.grist_doc_id+"/tables/Dn_data/records"
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.grist_pilotage_token
    }
    r = requests.put(url, headers=headers, data=get_grist_format(prestations))
    return r.json()

def get_grist_format(prestations: List[BlurredPrestation])-> str:
    grist_data = []
    for p in prestations:
        grist_data.append(
            {
                "require": {
                    "dossier_id": p.id
                },
                "fields": {
                    "matricule": p.matricule,
                    "affectation": p.affectation,
                    "decennie": p.decennie,
                    "genre": p.genre,
                    "type_prestation": p.type,
                    "montant_simulation": p.montant_simule
                }
            }
        )
    return json.dumps({"records": grist_data})
