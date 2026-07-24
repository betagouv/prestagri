import json

import requests
from typing import Any
from enum import Enum

from app.services.properties import properties

def get_pilotage_data() -> Any:
    return get_dn_dossiers()

def get_dn_dossiers() -> Any:
    url = "https://demarche.numerique.gouv.fr/api/v2/graphql"
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ demarche(number:'+  properties.dn_demarche_id +') { title dossiers { nodes {id champs { id label stringValue ... on RepetitionChamp { rows { champs {label stringValue} } } } annotations {label stringValue ... on RepetitionChamp { rows { champs {label stringValue} } } } } } } }"}'
    r = requests.post(url, headers=headers, data=data)
    return r.json()

def get_dn_dossier(dossier_number: str) -> Any:
    url = "https://demarche.numerique.gouv.fr/api/v2/graphql"
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ dossier(number: '+  dossier_number +') { id champs { id label stringValue ... on RepetitionChamp { rows { champs {label stringValue} } } } annotations {id label stringValue ... on RepetitionChamp { rows { champs {label stringValue} } } } } }"}'


    r = requests.post(url, headers=headers, data=data)
    return r.json()

def put_dn_annotation(dossier_number: str) -> Any:
    url = "https://demarche.numerique.gouv.fr/api/v2/graphql"
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "mutation { dossierModifierAnnotations () }"}'

    r = requests.post(url, headers=headers, data=data)
    return r.json()

class Champ(Enum):
    MATRICULE= "Q2hhbXAtNjYyNTkyOA=="
    AFFECTATION= "Q2hhbXAtNjM2MDYzMg=="
    BIRTHDATE= "Q2hhbXAtNjQyMDQwMA=="

def get_by_champ(dossier: Any, champ_id: Champ) -> str :
    for champ in dossier["champs"]:
        if champ["id"] == champ_id.value:
            return champ["stringValue"]
    return "information manquante"
