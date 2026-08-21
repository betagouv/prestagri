from app.services.blurring import blur_birthdate
from app.catala.generated.Aide_scolarite import CalculAideScolariteIn, calcul_aide_scolarite, calcul_quotient_familial_aide_scolarite, CalculQuotientFamilialAideScolariteIn
from app.catala.generated.Quotient_familial import CalculQuotientFamilialIn, calcul_quotient_familial
from app.catala.generated.Foyer_fiscal import FoyerFiscal
from app.catala.generated.Menage import Menage
from app.catala.generated.Trajet import Trajet
from app.catala.generated.catala_runtime import Option, Money, Integer
from app.model import Centimes


def test_blurring_age():
    assert blur_birthdate("12 juin 1987") == "1980"
