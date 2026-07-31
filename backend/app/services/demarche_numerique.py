import json

import requests
from typing import Any, List
from enum import Enum

from app.services.properties import properties

url= "https://demarche.numerique.gouv.fr/api/v2/graphql"

def get_pilotage_data() -> Any:
    return get_dn_dossiers()

def get_dn_dossiers() -> Any:
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ demarche(number:'+  properties.dn_demarche_id +') { title dossiers { nodes {id champs { id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } annotations {label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } } } } }"}'
    r = requests.post(url, headers=headers, data=data)
    return r.json()

def get_dn_dossier(dossier_number: str) -> Any :
    raw_data = retrieve_dn_dossier(dossier_number)
    return parse_dn_dossier(raw_data)

def retrieve_dn_dossier(dossier_number: str) -> Any:
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ dossier(number: '+  dossier_number +') { id champs { id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } annotations {id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } } }"}'


    r = requests.post(url, headers=headers, data=data)
    return r.json()

def parse_dn_dossier(dn_data: Any) -> Any:
    dossier = dn_data["data"]["dossier"]
    prestations = get_by_champ_id(dossier["champs"], Champ.PRESTATIONS, stringValue=False)["rows"]
    annotations = get_by_champ_id(dossier["annotations"], Champ.ANNOTATION_PRESTATION, stringValue=False)["rows"]

    return {
        "id": dossier["id"],
        "prestations": get_prestation_type_and_beneficiary(prestations),
        #"prestations-data": prestations,
        "annotations": get_prestation_type_and_beneficiary(annotations),
        #"annotations-data": annotations
        "raw": dn_data
    }

def get_prestation_type_and_beneficiary(prestations: List[Any]) -> Any:
    result = []
    for p in prestations:
        result.append({
            "type": get_by_champ_label(p["champs"], Champ.LABEL_TYPE_PRESTATION),
            "enfant": get_by_champ_label(p["champs"], Champ.LABEL_ENFANT_CONCERNE)
        })
    return result

def create_dn_annotations(dossier_id: str, number: int) -> Any:
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = {
        "query": "mutation dossierModifierAnnotations($input: DossierModifierAnnotationsInput!) { dossierModifierAnnotations(input: $input) { annotations { id label stringValue ... on RepetitionChamp { rows { champs { id label stringValue} } } } errors { message } clientMutationId } }",
        "variables": {
            "input": {
                "instructeurId": properties.dn_instructeurice_id,
                "dossierId": dossier_id,
                "annotations": [
                    {
                        "id": "Q2hhbXAtNjc3NjI1Mg==",
                        "value": {"repetition": number}
                    }
                ]
            }
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

class Champ(Enum):
    MATRICULE= "Q2hhbXAtNjYyNTkyOA=="
    AFFECTATION= "Q2hhbXAtNjM2MDYzMg=="
    BIRTHDATE= "Q2hhbXAtNjQyMDQwMA=="
    PRESTATIONS= "Q2hhbXAtNjU5NzU3MQ=="
    ANNOTATION_PRESTATION= "Q2hhbXAtNjc3NjI1Mg=="
    LABEL_TYPE_PRESTATION="Prestation demandée"
    LABEL_ENFANT_CONCERNE="Nom et prénom de l'enfant concerné"
    LABEL_ANNOTATION_TYPE_ENFANT="Commentaire"


def get_by_champ_id(dossier: Any, champ_id: Champ, stringValue:bool=True) -> Any :
    for champ in dossier:
        if champ["id"] == champ_id.value:
            if stringValue:
                return champ["stringValue"]
            else:
                return champ
    return "information manquante"

def get_by_champ_label(dossier: Any, label: Champ, stringValue:bool=True) -> Any:
    print(dossier)
    for champ in dossier:
        print(champ)
        if champ["label"] == label.value:
            if stringValue:
                return champ["stringValue"]
            else:
                return champ
    return "information manquante"
