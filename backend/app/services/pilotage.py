import requests
import json
from typing import Any

from app.services.properties import properties
from app.services.demarche_numerique import get_pilotage_data, get_by_champ, Champ
from app.services.blurring import blur_birthdate, blur_id

def upload_pilotage_data() -> Any:
    dn_data = get_pilotage_data()
    parsed_data = parse_pilotage_data(dn_data)
    uploaded = send_data_to_grist(parsed_data)
    return {
        "dn": dn_data,
        "parsed": parsed_data,
        "uploaded": uploaded
    }

def parse_pilotage_data(data: Any) -> Any:
    parsed = []
    dossiers = data["data"]["demarche"]["dossiers"]["nodes"]
    if len(dossiers) < 1:
        return  None
    for dossier in data["data"]["demarche"]["dossiers"]["nodes"]:
        parsed_dossier = {
            "require": {
                "dossier_id": blur_id(dossier["id"])
            },
            "fields": {
                "matricule": blur_id(get_by_champ(dossier, Champ.MATRICULE)),
                "affectation": get_by_champ(dossier, Champ.AFFECTATION),
                "decennie": blur_birthdate(get_by_champ(dossier, Champ.BIRTHDATE))
            }
        }
        parsed.append(parsed_dossier)

    return {"records": parsed}

def send_data_to_grist(parsed_data: Any) -> Any :
    if parsed_data is None:
        return {"explanation": "no data to upload"}
    url = "https://grist.numerique.gouv.fr/api/docs/"+properties.grist_doc_id+"/tables/Dn_data/records"
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.grist_pilotage_token
    }
    data = json.dumps(parsed_data)
    r = requests.put(url, headers=headers, data=data)
    return r.json()
