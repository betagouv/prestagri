import requests
import json
from typing import Any, List

from app.services.properties import properties
from app.services.demarche_numerique import get_pilotage_data
from app.services.blurring import blur_birthdate, blur_id, blur_date_to_year, blur_address, blur_date_to_month, blur_date_as_duration, blur_money_by_rounding
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
                mois_depot= blur_date_to_month(dn_dossier.date_depot),
                annee_depot= blur_date_to_year(dn_dossier.date_depot),
                delai_instruction= blur_date_as_duration(dn_dossier.date_depot, dn_dossier.date_instruction, dn_dossier.state),
                delai_dernier_changement= blur_date_as_duration(dn_dossier.date_instruction, dn_dossier.date_dernier_changement, dn_dossier.state),
                matricule=blur_id(dn_dossier.matricule),
                affectation=dn_dossier.affectation,
                category=dn_dossier.category,
                civilite=dn_dossier.civilite,
                departement=blur_address(dn_dossier.adresse),
                decennie=blur_birthdate(dn_dossier.date_naissance),
                type= prestation.type,
                revenu_fiscal= blur_money_by_rounding(float(dn_dossier.revenu_fiscal_reference), 1000) ,
                montant_simule=annotation.simulation_montant.value,
                montant_retenu=annotation.montant_retenu.value,
                qf_simule=blur_money_by_rounding(float(annotation.simulation_QF.value or 0 ), 50),
                qf_retenu=blur_money_by_rounding(float(annotation.qf_retenu.value or 0), 50)
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
                    "categorie": p.category,
                    "decennie": p.decennie,
                    "departement": p.departement,
                    "civilite": p.civilite,
                    "type_prestation": p.type,
                    "revenu_fiscal_reference": p.revenu_fiscal,
                    "montant_simulation": p.montant_simule,
                    "montant_retenu": p.montant_retenu,
                    "qf_simulation": p.qf_simule,
                    "qf_retenu": p.qf_retenu,
                    "mois_depot": p.mois_depot,
                    "annee_depot": p.annee_depot,
                    "delai_attente": p.delai_instruction,
                    "delai_traitement": p.delai_dernier_changement
                }
            }
        )
    return json.dumps({"records": grist_data})
