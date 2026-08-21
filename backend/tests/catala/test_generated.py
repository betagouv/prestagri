from app.catala.generated.Aide_scolarite import CalculAideScolariteIn, calcul_aide_scolarite, calcul_quotient_familial_aide_scolarite, CalculQuotientFamilialAideScolariteIn
from app.catala.generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from app.catala.generated.Foyer_fiscal import FoyerFiscal
from app.catala.generated.Menage import Menage
from app.catala.generated.Trajet import Trajet
from app.catala.generated.catala_runtime import Option, Money, Integer

def test_generated_catala_aide_scolarite():
    result = calcul_aide_scolarite(CalculAideScolariteIn(
        menage_agent_in= Menage(
            beneficiaire_porteur_handicap= True,
            garde_alternee= False,
            parent_isole= False,
            outre_mer= False,
            membres_du_foyer=[
                FoyerFiscal(
                    revenu_fiscal_reference=Money(3260000),
                    nombre_personnes=Integer(4)
                )
            ]
        ),
        etudiants_fiscalement_independants_in=[FoyerFiscal(
          revenu_fiscal_reference=Money(1000000),
            nombre_personnes=Integer(1)
        )],
        trajet_depuis_domicile_agent_in=Trajet(distance_km=Integer(100), duree_minutes=Integer(20)),
        trajet_depuis_domicile_etudiant_in=Option(None),
        montant_materiel_specifique_in=Money(100000),
        etudiant_en_filiere_post_bac_in= False
    ))

    assert float(result.quotient_familial) == 645.45
    assert float(result.revenu_fiscal_reference) == 42600

def test_generated_catala_quotient_familial_aide_scolarite():
    result = calcul_quotient_familial_aide_scolarite(CalculQuotientFamilialAideScolariteIn(
        menage_agent_in=Menage(
            beneficiaire_porteur_handicap=True,
            garde_alternee=False,
            parent_isole=False,
            outre_mer=False,
            membres_du_foyer=[
                FoyerFiscal(
                    revenu_fiscal_reference=Money(3260000),
                    nombre_personnes=Integer(4)
                )
            ]
        ),
        etudiants_fiscalement_independants_in=[FoyerFiscal(
            revenu_fiscal_reference=Money(1000000),
            nombre_personnes=Integer(1)
        )],
    ))

    assert float(result.quotient_familial) == 645.45
    assert float(result.revenu_fiscal_reference) == 42600

def test_generated_catala_quotient_familial():
    result = calcul_quotient_familial(CalculQuotientFamilialIn(
        menage_in=Menage(
            beneficiaire_porteur_handicap=True,
            garde_alternee=False,
            parent_isole=False,
            outre_mer=False,
            membres_du_foyer=[
                FoyerFiscal(
                    revenu_fiscal_reference=Money(4260000),
                    nombre_personnes=Integer(5)
                )
            ]
        )
    ))

    assert float(result.quotient_familial) == 645.45
    assert float(result.revenu_fiscal_reference) == 42600
