from app.services.aide_scolarite import get_aide_scolarite
from app.model import Menage, FoyerFiscal, Centimes, Trajet
from app.catala.aides import get_catala_quotient_familial_aide_scolarite

'''
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

    assert resultat.value == Centimes(valeur=0)
    assert resultat.explanation == {}

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

    assert resultat.value == Centimes(valeur=1000)
    assert resultat.explanation == {}

'''
