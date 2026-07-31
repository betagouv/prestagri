from typing import Any

from app.services.demarche_numerique import get_dn_dossier, create_dn_annotations

def upload_dossier_data(dossier_number: str) -> Any:
    dn_data = get_dn_dossier(dossier_number)
    created = create_annotations(dn_data)
    return {
        "created": created,
        "dn": dn_data,
        "uploaded": ""
    }

def create_annotations(dn_data: Any) -> Any:
    missing_annotations_number =  len(dn_data["prestations"]) - len(dn_data["annotations"])
    if missing_annotations_number > 0:
        return create_dn_annotations(dn_data["id"], missing_annotations_number)
    else:
        return {}
