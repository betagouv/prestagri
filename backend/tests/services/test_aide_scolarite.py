from app.services.aide_scolarite import get_aide_scolarite
from app.model import Menage, FoyerFiscal, Centimes, Trajet
from app.catala.aides import get_catala_quotient_familial_aide_scolarite

def test_get_aide_scolarite():
    resultat = get_aide_scolarite(
        Menage(beneficiaire_porteur_handicap=True,
               garde_alternee=False,
               parent_isole=False,
               outre_mer=False,
            membres=[FoyerFiscal(revenu=Centimes.from_euros_int(32600), personnes=4)]
        ),
        FoyerFiscal(revenu=Centimes.from_euros_int(10000), personnes=1),
        Trajet(distance_km=100, duree_min=20),
        None,
        Centimes.from_euros_int(1000),
        False
    )

    assert str(resultat.value) == '400.0€'
    assert resultat.explanation == {'aide_scolarite':
        {'critères_applicables_quotient_familial': "['Handicap : 0.5']",
         'calcul_quotient_familial': '42600.0€/ (12 x (5.0 + 0.5))',
         'quotient_familial': '645.45€',
         'critères_applicables_aide_scolarité': "['C3_eloignement_agent : 2.0', 'C4_materiel : 2.0']",
         'valeur_point': '100.0€',
         'calcul_aide_scolarité': '100.0€ x 4.0 = 400.0€'
         }
    }

def test_get_aide_scolarite_quotient_familial():
    resultat = get_catala_quotient_familial_aide_scolarite(
        Menage(beneficiaire_porteur_handicap=True,
               garde_alternee=False,
               parent_isole=False,
               outre_mer=False,
            membres=[
                FoyerFiscal(revenu=Centimes.from_euros_int(32600), personnes=4),
            ]
        ),
        [FoyerFiscal(revenu=Centimes.from_euros_int(10000), personnes=1)],
    )

    assert str(resultat.value) == '645.45€'
    assert resultat.explanation == {'calcul': '42600.0€/ (12 x (5.0 + 0.5))', 'critères_applicables': "['Handicap : 0.5']"}
