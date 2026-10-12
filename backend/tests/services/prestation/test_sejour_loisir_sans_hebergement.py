from datetime import date
from app.services.prestations.sejour import get_sejour_loisir_sans_hebergement
from app.model import Centimes
from tests.test_utils import create_menage_with_quotient

def test_classic():
    """Cas N°1 : séjour 3.5 jours classiques"""
    menage = create_menage_with_quotient(600)  # quotient familial = 600€
    resultat = get_sejour_loisir_sans_hebergement(
        menage=menage,
        date_naissance=date(year=2020, month=2, day=20),
        date_debut_sejour=date(year=2026, month=2, day=20),
        duree_sejour=3.5,
        montant_debourse=Centimes.from_euros_int(2000),
        centre_agree=True
    )
    # Expected: 30.30€ (from Catala test)
    assert str(resultat.value) == '30.30€'
    # Verify quotient familial is correctly set in explanation
    assert str(resultat.explanation["quotient_familial"]) == '600.00€'


def test_trop_age():
    """Cas N°2 : séjour enfant trop âgé"""
    menage = create_menage_with_quotient(600)
    resultat = get_sejour_loisir_sans_hebergement(
        menage=menage,
        date_naissance=date(year=1992, month=2, day=20),  # 34 years old in 2026
        date_debut_sejour=date(year=2026, month=2, day=20),
        duree_sejour=3.5,
        montant_debourse=Centimes.from_euros_int(2000),
        centre_agree=True
    )
    # Expected: 0.0€ (child is too old)
    assert str(resultat.value) == '0.00€'
    # Verify quotient familial is correctly set in explanation
    assert str(resultat.explanation["quotient_familial"]) == '600.00€'


def test_centre_non_agree():
    """Cas N°3 : séjour centre non agréé"""
    menage = create_menage_with_quotient(600)
    resultat = get_sejour_loisir_sans_hebergement(
        menage=menage,
        date_naissance=date(year=2020, month=2, day=20),
        date_debut_sejour=date(year=2026, month=2, day=20),
        duree_sejour=3.5,
        montant_debourse=Centimes.from_euros_int(2000),
        centre_agree=False
    )
    # Expected: 0.0€ (center not approved)
    assert str(resultat.value) == '0.00€'
    # Verify quotient familial is correctly set in explanation
    assert str(resultat.explanation["quotient_familial"]) == '600.00€'


def test_sejour_peu_cher():
    """Cas N°4 : séjour moins cher que l'aide"""
    menage = create_menage_with_quotient(600)
    resultat = get_sejour_loisir_sans_hebergement(
        menage=menage,
        date_naissance=date(year=2020, month=2, day=20),
        date_debut_sejour=date(year=2026, month=2, day=20),
        duree_sejour=3.5,
        montant_debourse=Centimes.from_euros_int(20),  # Very cheap stay
        centre_agree=True
    )
    # Expected: 20.0€ (aid capped at actual cost)
    assert str(resultat.value) == '20.00€'
    # Verify quotient familial is correctly set in explanation
    assert str(resultat.explanation["quotient_familial"]) == '600.00€'


def test_famille_aisée():
    """Cas N°5 : famille aisée"""
    menage = create_menage_with_quotient(2000)  # High quotient familial
    resultat = get_sejour_loisir_sans_hebergement(
        menage=menage,
        date_naissance=date(year=2020, month=2, day=20),
        date_debut_sejour=date(year=2026, month=2, day=20),
        duree_sejour=3.5,
        montant_debourse=Centimes.from_euros_int(2000),
        centre_agree=True
    )
    # Expected: 0.0€ (family too wealthy)
    assert str(resultat.value) == '0.00€'
    # Verify quotient familial is correctly set in explanation
    assert str(resultat.explanation["quotient_familial"]) == '2000.00€'
