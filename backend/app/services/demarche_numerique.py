import json

import requests
from typing import Any, List
from enum import Enum

from app.services.properties import properties

url= "https://demarche.numerique.gouv.fr/api/v2/graphql"

def get_pilotage_data() -> Any:
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ demarche(number:'+  properties.dn_demarche_id +') { title dossiers { nodes {id champs { id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } annotations {label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } } } } }"}'
    r = requests.post(url, headers=headers, data=data)
    return r.json()

def get_dn_dossier(dossier_number: str) -> Any:
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ dossier(number: '+  dossier_number +') { id champs { id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } annotations {id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } } }"}'


    r = requests.post(url, headers=headers, data=data)
    return parse_dn_dossier(r.json())

def parse_dn_dossier(dn_data: Any) -> Any:
    dossier = dn_data["data"]["dossier"]
    prestations = get_by_champ_id(dossier["champs"], Champ.PRESTATIONS)["rows"]
    annotations = get_by_champ_id(dossier["annotations"], Champ.ANNOTATION_PRESTATION)["rows"]

    return {
        "id": dossier["id"],
        "prestations": get_prestation_type_and_beneficiary(prestations),
        "annotations": get_prestation_type_and_beneficiary(annotations, True),
        "raw": dn_data
    }

def get_prestation_type_and_beneficiary(prestations: List[Any], is_annotation: bool = False) -> Any:
    result = []
    for p in prestations:
        parsed = {
            #"raw": p,
            "id": {
                        "id": "non relevant information",
                        "value": get_by_champ_label(p["champs"], Champ.LABEL_TYPE_PRESTATION)["id"],
                    },

            "type": get_by_champ_label(p["champs"], Champ.LABEL_TYPE_PRESTATION),
            "enfant": get_by_champ_label(p["champs"], Champ.LABEL_ENFANT_CONCERNE),
            "beneficiaire": get_by_champ_label(p["champs"], Champ.LABEL_BENEFICIAIRE),
        }
        if is_annotation:
            parsed["associated_prestation"] = get_by_champ_label(p["champs"], Champ.LABEL_ASSOCIATED_PRESTATION)
            parsed["simulation_montant"] = get_by_champ_label(p["champs"], Champ.LABEL_SIMULATION_AMOUNT)
            parsed["simulation_explication"] = get_by_champ_label(p["champs"], Champ.LABEL_SIMULATION_EXPLANATION)


        result.append(parsed)
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
    raw = r.json()
    annotations = get_by_champ_id(raw["data"]["dossierModifierAnnotations"]["annotations"], Champ.ANNOTATION_PRESTATION)["rows"]
    return get_prestation_type_and_beneficiary(annotations, True)

def fill_dn_text(dossier_id: str, field_id: str, value: str) -> Any:
    return fill_dn_field(dossier_id, field_id, {"text" : value})

def fill_dn_simple_choice(dossier_id: str, field_id: str, value: str) -> Any:
    return fill_dn_field(dossier_id, field_id, {"dropDownList" : value})

def fill_dn_field(dossier_id: str, field_id: str, value: Any) -> Any:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + properties.dn_pilotage_token
    }
    data = {
        "query": "mutation dossierModifierAnnotations($input: DossierModifierAnnotationsInput!) { dossierModifierAnnotations(input: $input) { annotations { id label stringValue ... on RepetitionChamp { rows { champs { id label stringValue} } } } errors { message } clientMutationId } }",
        "variables": {
            "input": {
                "instructeurId": properties.dn_instructeurice_id,
                "dossierId": dossier_id,
                "annotations": [
                    {
                        "id": field_id,
                        "value": value
                    }
                ]
            }
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

class Champ(Enum):
    ID="id"
    MATRICULE= "Q2hhbXAtNjYyNTkyOA=="
    AFFECTATION= "Q2hhbXAtNjM2MDYzMg=="
    BIRTHDATE= "Q2hhbXAtNjQyMDQwMA=="
    PRESTATIONS= "Q2hhbXAtNjU5NzU3MQ=="
    ANNOTATION_PRESTATION= "Q2hhbXAtNjc3NjI1Mg=="
    LABEL_TYPE_PRESTATION="Prestation demandée"
    LABEL_ENFANT_CONCERNE="Nom et prénom de l'enfant concerné"
    LABEL_BENEFICIAIRE="Bénéficiaire"
    LABEL_ANNOTATION_TYPE_ENFANT="Commentaire"
    LABEL_ASSOCIATED_PRESTATION="Id de la prestation correspondante"
    LABEL_SIMULATION_AMOUNT="Montant calculé par simulation"
    LABEL_SIMULATION_EXPLANATION="Explication de la simulation"



def get_by_champ_id(dossier: Any, champ_id: Champ) -> Any :
    for champ in dossier:
        if champ["id"] == champ_id.value:
            return champ
    return {"id": "information manquante", "value" : "information manquante"}

def get_by_champ_label(dossier: Any, label: Champ, stringValue:bool=True) -> Any:
    for champ in dossier:
        if champ["label"] == label.value:
            if stringValue:
                return {
                    "id": champ["id"],
                    "value" : champ["stringValue"]
                }
            else:
                return champ
    return {"id": "information manquante", "value" : "information manquante"}
