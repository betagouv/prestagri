from app.catala.generated.Aide_scolarite import CalculAideScolariteIn, calcul_aide_scolarite, calcul_quotient_familial_aide_scolarite, CalculQuotientFamilialAideScolariteIn
from app.catala.generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from app.catala.generated.Foyer_fiscal import FoyerFiscal
from app.catala.generated.Menage import Menage
from app.catala.generated.Trajet import Trajet
from app.catala.generated.catala_runtime import Option, Money, Integer

def test_generated_catala_aide_scolarite():
    result = calcul_aide_scolarite(CalculAideScolariteIn(
        foyer_fiscal_agent_in= Menage(
            beneficiaire_porteur_handicap= True,
            garde_alternee= False,
            parent_isole= False,
            outre_mer= False,
            membres_du_foyer=[
                FoyerFiscal(
                    revenu_fiscal_reference=Money(32600),
                    nombre_personnes=Integer(4)
                )
            ]
        ),
        etudiants_fiscalement_independants_in=[FoyerFiscal(
          revenu_fiscal_reference=Money(10000),
            nombre_personnes=Integer(1)
        )],
        trajet_depuis_domicile_agent_in=Trajet(distance_km=Integer(100), duree_minutes=Integer(20)),
        trajet_depuis_domicile_etudiant_in=Option(None),
        montant_materiel_specifique_in=Money(1000),
        etudiant_en_filiere_post_bac_in= False
    ))

    assert result.quotient_familial == 64545
    assert result.revenu_fiscal_reference == 42600

def test_generated_catala_quotient_familial_aide_scolarite():
    result = calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(
        foyer_fiscal_agent_in=Menage(
            beneficiaire_porteur_handicap=True,
            garde_alternee=False,
            parent_isole=False,
            outre_mer=False,
            membres_du_foyer=[
                FoyerFiscal(
                    revenu_fiscal_reference=Money(32600),
                    nombre_personnes=Integer(4)
                )
            ]
        ),
        etudiants_fiscalement_independants_in=[FoyerFiscal(
            revenu_fiscal_reference=Money(10000),
            nombre_personnes=Integer(1)
        )],
    ))

    assert result.quotient_familial == 64545
    assert result.revenu_fiscal_reference == 42600

def test_generated_catala_quotient_familial():
    result = calcul_quotient_familial(CalculQuotientFamilialIn(
        menage_in=Menage(
            beneficiaire_porteur_handicap=True,
            garde_alternee=False,
            parent_isole=False,
            outre_mer=False,
            membres_du_foyer=[
                FoyerFiscal(
                    revenu_fiscal_reference=Money(42600),
                    nombre_personnes=Integer(5)
                )
            ]
        )
    ))

    assert result.quotient_familial == 64545
    assert result.revenu_fiscal_reference == 42600
