from app.catala.aides import get_catala_aide_scolarite
from app.model import Response, Menage, Centimes, FoyerFiscal, Trajet

def get_aide_scolarite(
    menage: Menage,
    etudiant_fiscalement_independant: FoyerFiscal | None,
    trajet_domicile_agent: Trajet,
    trajet_domicile_etudiant: Trajet | None = None,
    montant_materiel_specifique: Centimes | None = None,
    etudiant_post_bac: bool = False ) -> Response[Centimes]:

    etudiants_independants = []
    if etudiant_fiscalement_independant is not None:
        etudiants_independants.append(etudiant_fiscalement_independant)

    aide_scolarite = get_catala_aide_scolarite(
        menage,
        etudiants_independants,
        trajet_domicile_agent,
        trajet_domicile_etudiant,
        montant_materiel_specifique or Centimes(valeur=0),
        etudiant_post_bac)

    explanation = {
        "aide_scolarite": aide_scolarite.explanation
    }

    return Response[Centimes](value=aide_scolarite.value, explanation=explanation)
