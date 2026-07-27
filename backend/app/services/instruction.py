from typing import Any

from app.services.demarche_numerique import get_dn_dossier


def upload_dossier_data(dossier_number: str) -> Any:
    dn_data = get_dn_dossier(dossier_number)
    return {
        "dn": dn_data,
        "uploaded": ""
    }
