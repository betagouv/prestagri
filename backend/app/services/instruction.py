from typing import Any, List
from app.services.demarche_numerique import get_dn_dossier, create_dn_annotations, fill_dn_short_text, fill_dn_simple_choice, fill_dn_long_text, fill_dn_decimal
from app.model import DNDossier, Annotation, Prestation, Centimes, Response, PrestationType
from app.services.aide_scolarite import get_aide_scolarite, format_explanation
from app.services.prestations.handicap import get_aide_handicap_moins_20ans


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
        fill_dn_short_text(dossier_id, annotation.beneficiaire.id, prestation.enfant)
        fill_dn_simple_choice(dossier_id, annotation.type.id, prestation.type)
        fill_dn_short_text(dossier_id, annotation.associated_prestation_id.id, prestation.id)
        response = Response(value=Centimes(valeur=0), explanation={"quotient_familial" : "non connu pour cette prestation"})
        if prestation.type == PrestationType.AIDE_SCOLARITE.value:
            response = compute_aide_scolarite(prestation)
        if prestation.type == PrestationType.ENFANT_HANDICAP.value:
            response = compute_aide_handicap_moins_20ans(prestation)

        fill_dn_short_text(dossier_id, annotation.simulation_QF.id, str(response.explanation["quotient_familial"]))
        fill_dn_short_text(dossier_id, annotation.simulation_montant.id, str(float(response.value)))
        fill_dn_long_text(dossier_id, annotation.simulation_explication.id, format_explanation(response.explanation))

    return associated_annotations


def compute_aide_scolarite(prestation: Prestation) -> Response[Centimes]:
    data = prestation.calcul_data
    return get_aide_scolarite(
        menage=data["menage"],
        etudiant_fiscalement_independant=data["etudiant_fiscalement_independant"],
        trajet_domicile_agent=data["trajet_domicile_agent"],
        trajet_domicile_etudiant=data["trajet_domicile_etudiant"],
        montant_materiel_specifique=data["montant_materiel_specifique"],
        etudiant_post_bac=data["etudiant_post_bac"]
    )

def compute_aide_handicap_moins_20ans(prestation: Prestation) -> Response[Centimes]:
    data = prestation.calcul_data
    return get_aide_handicap_moins_20ans (
        annee_demandee=data["annee_demandee"],
        date_naissance=data["date_naissance"],
        date_fin_validite=data["date_fin_validite"],
        pourcentage_incapacite_permanente=data["pourcentage_incapacite_permanente"],
        pourcentage_hors_internat=100-data["pourcentage_en_internat"],
    )

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
