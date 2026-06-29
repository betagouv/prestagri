from app.catala.aides import get_catala_quotient_familial_aide_scolarite, get_catala_criteres_eligibles_aide_scolarite, get_catala_aide_scolarite
from app.model import Response, Menage, Centimes, FoyerFiscal
from app.services.gps import get_trajet


def get_aide_scolarite(
    Menage: Menage,
    etudiant_fiscalement_independant: FoyerFiscal | None,
    adresse_agent: str,
    adresse_etablissement: str,
    adresse_etudiant: str | None = None,
    montant_materiel_specifique: Centimes | None = None,
    etudiant_post_bac: bool = False) -> Response[Centimes]:

    etudiants_independants = []
    if etudiant_fiscalement_independant is not None:
        etudiants_independants.append(etudiant_fiscalement_independant)
    quotient_familial_scolarite = get_catala_quotient_familial_aide_scolarite(Menage, etudiants_independants)

    trajet_domicile_agent = get_trajet(adresse_agent, adresse_etablissement)
    trajet_domicile_etudiant = get_trajet(adresse_etudiant, adresse_etablissement) if adresse_etudiant is not None else None
    nb_points = get_catala_criteres_eligibles_aide_scolarite(
        trajet_domicile_agent,
        trajet_domicile_etudiant,
        montant_materiel_specifique or Centimes(valeur=0),
        quotient_familial_scolarite.value,
        etudiant_post_bac
    )
    aide_scolarite = get_catala_aide_scolarite(quotient_familial_scolarite.value, nb_points.value)

    explanation = {
        "quotient_familial": quotient_familial_scolarite.explanation,
        "criteres_eligibles": nb_points.explanation,
        "aide_scolarite": aide_scolarite.explanation
    }

    return Response[Centimes](value=aide_scolarite.value, explanation=str(explanation))
