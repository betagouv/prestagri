from app.services.quotient_familial import get_quotient_familial
from app.model import Menage, FoyerFiscal, Centimes, Trajet

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

    assert str(resultat.value) == '493.94€'
    assert resultat.explanation == {'calcul': '32600.0€/ (12 x (5.0 + 0.5))', 'critères_applicables': "['Handicap : 0.5']"}
