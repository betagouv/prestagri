import requests
from ..services.properties import properties
from typing import Any

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
