import requests
import json
from ..services.properties import properties
from typing import Any


def upload_pilotage_data() -> Any:
    dn_data = get_dn_dossiers()
    parsed_data = parse_dn_data(dn_data)
    uploaded = send_data_to_grist(parsed_data)
    return {
       # "dn": dn_data,
       # "parsed_data": parsed_data,
        "uploaded": uploaded
    }


# see https://demarche.numerique.gouv.fr/graphql to create a GraphQL Query

## Bash
# curl \
#-H 'Content-Type: application/json' \
#-H 'Authorization: Bearer **see key in shell.nix or var env' \
#--data '{ "query": "{ demarche(number: 146454) { title dossiers { nodes {id champs { label stringValue } annotations {label stringValue } } } } }" }' \
#'https://demarche.numerique.gouv.fr/api/v2/graphql'

def get_dn_dossiers() -> Any:

    url = "https://demarche.numerique.gouv.fr/api/v2/graphql"
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ demarche(number: 146454) { title dossiers { nodes {id champs { label stringValue ... on RepetitionChamp { rows { champs {label stringValue} } } } annotations {label stringValue ... on RepetitionChamp { rows { champs {label stringValue} } } } } } } }"}'
    r = requests.post(url, headers=headers, data=data)
    return r.json()

## Bash

#curl -X 'PUT' \
#  'https://grist.numerique.gouv.fr/api/docs/**doc_id***/tables/Dn_data/records' \
#  -H 'accept: */*' \
#  -H 'Authorization: Bearer XXXXXXXXXXX' \
#  -H 'Content-Type: application/json' \
#  -d ''

def parse_dn_data(data: Any) -> Any:
    return {
        "records": [
            {
            "require": {
                "pet": "cat"
            },
            "fields": {
                "popularity": 67
            }
            },
            {
            "require": {
                "pet": "dog"
            },
            "fields": {
                "popularity": 95
            }
            }
        ]
    }



def send_data_to_grist(parsed_data: Any) -> Any :

    url = "https://grist.numerique.gouv.fr/api/docs/"+properties.grist_doc_id+"/tables/Dn_data/records"
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.grist_pilotage_token
    }
    data = json.dumps(parsed_data)
    r = requests.put(url, headers=headers, data=data)
    return r.json()
