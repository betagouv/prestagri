from typing import Any, List
from app.services.demarche_numerique import get_dn_dossier, create_dn_annotations, fill_dn_text, fill_dn_simple_choice

def upload_dossier_data(dossier_number: str) -> Any:
    dn_data = get_dn_dossier(dossier_number)
    dossier_id = dn_data["id"]
    created = create_annotations(dossier_id, dn_data)
    annotations = created if created else dn_data["annotations"]
    filled = fill_annotation(dossier_id, dn_data["prestations"], annotations)
    return {
        "filled": filled,
        "created": created,
        "dn": dn_data,
    }

def create_annotations(dossier_id: str, dn_data: Any) -> Any:
    missing_annotations_number =  len(dn_data["prestations"]) - len(dn_data["annotations"])
    return create_dn_annotations(dossier_id, missing_annotations_number) if missing_annotations_number > 0 else {}

def fill_annotation(dossier_id: str, prestations:List[Any], annotations: List[Any]) -> Any:
    associated_annotations = identify_associated_annotations(prestations, annotations)
    for prestation_id in associated_annotations.keys():
        (prestation, annotation) = associated_annotations[prestation_id]
        fill_dn_text(dossier_id, annotation["beneficiaire"]["id"], prestation["enfant"]["value"])
        fill_dn_text(dossier_id, annotation["associated_prestation"]["id"], prestation["id"]["value"])
        fill_dn_text(dossier_id, annotation["simulation_explication"]["id"], "Explication et calcul à venir")
        fill_dn_simple_choice(dossier_id, annotation["type"]["id"], prestation["type"]["value"])
    return associated_annotations



#TODO To improved - rushed before demo test
def identify_associated_annotations(prestations:List[Any], annotations: List[Any]) -> dict[str, tuple[Any, Any]]:
    associated_annotations = {}
    unassociated_prestation = prestations
    for a in annotations:
        a_id = a["id"]["value"]
        prestation_id = a["associated_prestation"]["value"]
        for p in unassociated_prestation:
            if p["id"]["value"] == prestation_id:
                associated_annotations[a_id] = (p,a)
                unassociated_prestation.remove(p)
    for a in annotations:
        a_id = a["id"]["value"]
        if a_id not in associated_annotations.keys():
            associated_annotations[a_id] = (unassociated_prestation.pop(), a)
    return associated_annotations
