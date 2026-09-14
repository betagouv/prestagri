from datetime import date
from app.services.prestations.handicap import get_aide_handicap_moins_20ans, format_explanation

def test_get_aide_handicap():
    resultat = get_aide_handicap_moins_20ans(
        annee_demandee=2026,
        date_naissance= date(year=2016, month=3, day=8),
        date_fin_validite= date(year=2028, month=12, day=12),
        pourcentage_incapacite_permanente= 80,
        pourcentage_hors_internat= 70
    )

    assert str(resultat.value) == '183.0€'
    assert format_explanation(resultat.explanation) == {
        'versement': "['Handicap : 0.5']",
        '': '42600.0€/ (12 x (5.0 + 0.5))',
        'quotient_familial': '645.45€',
        'critères_applicables_aide_scolarité': "['C3_eloignement_agent : 2.0', 'C4_materiel : 2.0']",
        'valeur_point': '100.0€',
        'calcul_aide_scolarité': '100.0€ x 4.0 = 400.0€'
    }
