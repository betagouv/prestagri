from app.services.quotient_familial import get_quotient_familial
from app.model import Menage, FoyerFiscal, Centimes, Trajet

'''
def test_get_quotient_familial():
    resultat = get_quotient_familial(
        Menage(beneficiaire_porteur_handicap=True,
               garde_alternee=False,
               parent_isole=False,
               outre_mer=False,
            membres=[
                FoyerFiscal(revenu=Centimes.from_euros_int(32600), personnes=4),
                FoyerFiscal(revenu=Centimes(valeur=0), personnes=1),
            ]
        )
    )

    assert resultat.value == Centimes(valeur=1000)
    assert resultat.explanation == {}
'''
