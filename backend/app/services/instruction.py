from typing import Any, List
from app.services.demarche_numerique import get_dn_dossier, create_dn_annotations, fill_dn_text, fill_dn_simple_choice
from app.model import DNDossier, Annotation, Prestation

def prefill_dossier_annotations(dossier_number: str) -> Any:
    dn_dossier = get_dn_dossier(dossier_number)
    created = create_annotations(dn_dossier.id, dn_dossier)
    annotations = created if created else dn_dossier.annotations
    filled = fill_annotations(dn_dossier.id, dn_dossier.prestations, annotations)
    return {
        "filled": filled,
        "created": created,
        "dn": dn_dossier,
    }

def create_annotations(dossier_id: str, dn_dossier: DNDossier) -> List[Annotation]:
    missing_annotations_number = len(dn_dossier.prestations) - len(dn_dossier.annotations)
    return create_dn_annotations(dossier_id, missing_annotations_number) if missing_annotations_number > 0 else []

def fill_annotations(dossier_id: str, prestations:List[Prestation], annotations: List[Annotation]) -> Any:
    associated_annotations = identify_associated_annotations(prestations, annotations)
    for prestation_id in associated_annotations.keys():
        (prestation, annotation) = associated_annotations[prestation_id]
        fill_dn_text(dossier_id, annotation.beneficiaire.id, prestation.enfant)
        fill_dn_text(dossier_id, annotation.associated_prestation_id.id, prestation.id)
        fill_dn_text(dossier_id, annotation.simulation_explication.id, "Explication et calcul à venir")
        fill_dn_simple_choice(dossier_id, annotation.type.id, prestation.type)
    return associated_annotations

#TODO To improved - rushed before demo test
def identify_associated_annotations(prestations:List[Prestation], annotations: List[Annotation]) -> dict[str, tuple[Prestation, Annotation]]:
    associated_prestation = {}
    unassociated_annotation = annotations
    for p in prestations:
        for a in unassociated_annotation:
            if p.id == a.associated_prestation_id:
                associated_prestation[p.id] = (p, a)
                unassociated_annotation.remove(a)
    for p in prestations:
        if p.id not in associated_prestation.keys():
            associated_prestation[p.id] = (p, unassociated_annotation.pop())
    return associated_prestation
