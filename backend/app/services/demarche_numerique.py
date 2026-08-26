import json

import requests
from typing import Any, List
from enum import Enum

from app.services.properties import properties
from app.model import Menage, FoyerFiscal, Trajet, Annotation, Prestation, Champ, DNDossier, Centimes
from app.utils import to_bool

MISSING_DATA = "information manquante"
url= "https://demarche.numerique.gouv.fr/api/v2/graphql"

def get_pilotage_data() -> Any:
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ demarche(number:'+  properties.dn_demarche_id +') { title dossiers { nodes {id champs { id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } annotations {label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } } } } }"}'
    r = requests.post(url, headers=headers, data=data)
    return r.json()

def get_dn_dossier(dossier_number: str) -> DNDossier:
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + properties.dn_pilotage_token
    }
    data = '{ "query": "{ dossier(number: '+  dossier_number +') { id champs { id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } annotations {id label stringValue ... on RepetitionChamp { rows { champs {id label stringValue} } } } } }"}'


    r = requests.post(url, headers=headers, data=data)
    return parse_dn_dossier(r.json())

def create_dn_annotations(dossier_id: str, number: int) -> List[Annotation]:
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
    annotations = get_champ_repetable_by_label(raw["data"]["dossierModifierAnnotations"]["annotations"], ChampLabel.LABEL_INSTRUCTION_REPETABLE)
    return parse_annotation(annotations)

def fill_dn_decimal(dossier_id: str, field_id: str, value: str) -> Any:
    return fill_dn_field(dossier_id, field_id, {"decimalNumber" : value})


def fill_dn_short_text(dossier_id: str, field_id: str, value: str) -> Any:
    return fill_dn_field(dossier_id, field_id, {"text" : value})

def fill_dn_long_text(dossier_id: str, field_id: str, value: str) -> Any:
    return fill_dn_field(dossier_id, field_id, {"textarea" : value})


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

class ChampLabel(Enum):
    MATRICULE="Q2hhbXAtNjYyNTkyOA=="
    AFFECTATION="Q2hhbXAtNjM2MDYzMg=="
    BIRTHDATE="Q2hhbXAtNjQyMDQwMA=="
    LABEL_INSTRUCTION_REPETABLE="Instruction de prestation"
    LABEL_PRESTATION_REPETABLE ="Prestation"
    LABEL_TYPE_PRESTATION="Quelle prestation demandez-vous ?"
    LABEL_ANNOTATION_TYPE_PRESTATION="Type de prestation demandée"
    LABEL_ENFANT_CONCERNE="Nom et prénom de l'enfant concerné"
    LABEL_BENEFICIAIRE="Bénéficiaire"
    LABEL_ANNOTATION_TYPE_ENFANT="Commentaire"
    LABEL_ASSOCIATED_PRESTATION="Identifiant de prestation"
    LABEL_SIMULATION_AMOUNT="Montant calculé par simulation"
    LABEL_SIMULATION_EXPLANATION="Explication de la simulation"
    LABEL_ENFANT_PORTEUR_HANDICAP="L'enfant est il porteur d'un handicap ?"
    LABEL_ENFANT_GARDE_ALTERNEE="L'enfant est-il en garde alternée ?"
    LABEL_PARENT_ISOLE="Êtes-vous un parent isolé ?"
    LABEL_OUTRE_MER="Résidez vous en Outre-Mer ?"
    LABEL_REVENU_FISCAL="Revenu fiscal de référence (arrondi à l'euro)"
    LABEL_AVIS_IMPOTS_DEPENDANTS="Nombre de personnes rattachées à l'avis d'imposition"
    LABEL_REVENU_FISCAL_ENFANT="Revenu fiscal de référence de l'enfant (arrondi à l'euro)"
    LABEL_AVIS_IMPOTS_DEPENDANTS_ENFANT="Nombre de personnes rattachées à l'avis d'imposition de l'enfant"
    LABEL_DISTANCE_AGENT_ECOLE="Quelle est la distance entre votre logement et l'établissement scolaire de votre enfant (en km)"
    LABEL_DUREE_AGENT_ECOLE="Quelle est la durée du trajet entre votre logement et l'établissement scolaire de votre enfant (en min)"
    LABEL_DISTANCE_ENFANT_ECOLE="Quelle est la distance entre le logement de votre enfant et son établissement scolaire (en km))"
    LABEL_DUREE_ENFANT_ECOLE="Quelle est la durée du trajet entre le logement de votre enfant et son établissement scolaire (en min)"
    LABEL_MATERIEL_SPECIFIQUE="Quel est le montant total des factures acquittées ? (arrondi à l'euros près)"
    LABEL_ENFANT_ETUDES_SUPERIEURES="Votre enfant est-il un étudiant en études supérieures ?"

def get_champ_by_label(dossier: Any, label: ChampLabel) -> Champ:
    for champ in dossier:
        if champ["label"] == label.value:
            return Champ(
                id= champ["id"],
                value= champ["stringValue"]
            )
    return Champ(id= MISSING_DATA, value= MISSING_DATA)

def get_champ_repetable_by_label(dossier: Any, label: ChampLabel) -> List[Any]:
    for champ in dossier:
        if champ["label"] == label.value:
            return champ["rows"]
    return []


def parse_dn_dossier(dn_data: Any) -> DNDossier:
    dossier = dn_data["data"]["dossier"]
    prestations = get_champ_repetable_by_label(dossier["champs"], ChampLabel.LABEL_PRESTATION_REPETABLE)
    annotations = get_champ_repetable_by_label(dossier["annotations"], ChampLabel.LABEL_INSTRUCTION_REPETABLE)

    return DNDossier(
        id = dossier["id"],
        prestations= parse_prestation(prestations, dossier),
        annotations= parse_annotation(annotations),
        raw= dn_data
    )

def parse_prestation(prestations: List[Any], dossier: Any) -> List[Prestation]:
    result = []
    for p in prestations:
        champs = p["champs"]
        prestation = Prestation(
            id= get_champ_by_label(champs, ChampLabel.LABEL_TYPE_PRESTATION).id,
            type= get_champ_by_label(champs, ChampLabel.LABEL_TYPE_PRESTATION).value,
            enfant= get_champ_by_label(champs, ChampLabel.LABEL_ENFANT_CONCERNE).value,
            calcul_data= {}
        )
        if prestation.type  == "Aide a la scolarité":
            prestation.calcul_data = parse_data_for_aide_scolarite_data(p, dossier)
        result.append(prestation)
    return result

def parse_annotation(annotations: List[Any]) -> List[Annotation]:
    result = []
    for a in annotations:
        champs = a["champs"]
        result.append(Annotation(
            type=get_champ_by_label(champs, ChampLabel.LABEL_ANNOTATION_TYPE_PRESTATION),
            beneficiaire=get_champ_by_label(champs, ChampLabel.LABEL_BENEFICIAIRE),
            associated_prestation_id= get_champ_by_label(champs, ChampLabel.LABEL_ASSOCIATED_PRESTATION),
            simulation_montant= get_champ_by_label(champs, ChampLabel.LABEL_SIMULATION_AMOUNT),
            simulation_explication= get_champ_by_label(champs, ChampLabel.LABEL_SIMULATION_EXPLANATION)
        ))
    return result

def parse_data_for_aide_scolarite_data(raw_prestation: Any, raw_dn_dossier: Any) -> Any:
    """
    parsed = menage: Menage,
    etudiant_fiscalement_independant: FoyerFiscal | None,
    trajet_domicile_agent: Trajet,
    trajet_domicile_etudiant: Trajet | None = None,
    montant_materiel_specifique: Centimes | None = None,
    etudiant_post_bac: bool = False
    """
    menage = Menage(
        beneficiaire_porteur_handicap=to_bool(get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_ENFANT_PORTEUR_HANDICAP).value),
        garde_alternee=to_bool(get_champ_by_label(raw_dn_dossier["champs"], ChampLabel.LABEL_ENFANT_GARDE_ALTERNEE).value),
        parent_isole=to_bool(get_champ_by_label(raw_dn_dossier["champs"], ChampLabel.LABEL_PARENT_ISOLE).value),
        outre_mer=to_bool(get_champ_by_label(raw_dn_dossier["champs"], ChampLabel.LABEL_OUTRE_MER).value),
        membres=[FoyerFiscal(
            revenu=Centimes.from_euros_int(int(get_champ_by_label(raw_dn_dossier["champs"], ChampLabel.LABEL_REVENU_FISCAL).value)),
            personnes=int(get_champ_by_label(raw_dn_dossier["champs"], ChampLabel.LABEL_AVIS_IMPOTS_DEPENDANTS).value)
        )]
    )
    revenu_fiscal_enfant = get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_REVENU_FISCAL_ENFANT).value
    etudiant_fiscalement_independant = None if (revenu_fiscal_enfant == MISSING_DATA) else FoyerFiscal(
        revenu=Centimes.from_euros_int(int(revenu_fiscal_enfant)),
        personnes=int(get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_AVIS_IMPOTS_DEPENDANTS_ENFANT).value)
    )

    trajet_domicile_agent = Trajet(
        distance_km=int(get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_DISTANCE_AGENT_ECOLE).value),
        duree_min=int(get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_DUREE_AGENT_ECOLE).value),
    )

    duree_trajet_domicile_enfant = get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_DUREE_ENFANT_ECOLE).value
    trajet_domicile_etudiant = None if duree_trajet_domicile_enfant == MISSING_DATA else Trajet(
        distance_km=int(get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_DISTANCE_ENFANT_ECOLE).value),
        duree_min=int(duree_trajet_domicile_enfant),
    )

    champ_materiel_specifique = get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_MATERIEL_SPECIFIQUE).value
    montant_materiel_specifique= None if champ_materiel_specifique == MISSING_DATA else Centimes.from_euros_int(int(champ_materiel_specifique))
    etudiant_post_bac = to_bool(get_champ_by_label(raw_prestation["champs"], ChampLabel.LABEL_ENFANT_ETUDES_SUPERIEURES).value)
    return {
        "menage" : menage,
        "etudiant_fiscalement_independant": etudiant_fiscalement_independant,
        "trajet_domicile_agent": trajet_domicile_agent,
        "trajet_domicile_etudiant": trajet_domicile_etudiant,
        "montant_materiel_specifique": montant_materiel_specifique,
        "etudiant_post_bac": etudiant_post_bac
    }
