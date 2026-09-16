from datetime import date
from app.services.prestations.handicap import get_aide_handicap_moins_20ans
from app.model import Versement, Centimes

def test_classic():
    resultat = get_aide_handicap_moins_20ans(
        annee_demandee=2026,
        date_naissance= date(year=2014, month=9, day=12),
        date_fin_validite= date(year=2028, month=10, day=23),
        pourcentage_incapacite_permanente= 70,
        pourcentage_hors_internat= 100
    )

    assert str(resultat.value) == '183.0€'
    assert resultat.explanation == {
        "versements": [
            Versement(date=date(2026, 6, 1), montant=Centimes(valeur=54900)),
            Versement(date=date(2026, 9, 1), montant=Centimes(valeur=54900)),
            Versement(date=date(2026,12, 1), montant = Centimes(valeur=54900)),
            Versement(date=date(2027, 3, 1), montant=Centimes(valeur=54900))
        ],
        "alerte_derniere_annee": False
    }

def test_trop_age():
    resultat = get_aide_handicap_moins_20ans(
        annee_demandee=2026,
        date_naissance= date(year=2004, month=9, day=12),
        date_fin_validite= date(year=2028, month=10, day=23),
        pourcentage_incapacite_permanente= 60,
        pourcentage_hors_internat= 100
    )

    assert str(resultat.value) == '0.0€'
    assert resultat.explanation == {
        "versements": [],
        "alerte_derniere_annee": False
    }

def test_20_this_year():
    resultat = get_aide_handicap_moins_20ans(
        annee_demandee=2026,
        date_naissance= date(year=2006, month=9, day=12),
        date_fin_validite= date(year=2028, month=10, day=23),
        pourcentage_incapacite_permanente= 60,
        pourcentage_hors_internat= 100
    )

    assert str(resultat.value) == '183.0€'
    assert resultat.explanation == {
        "versements": [
            Versement(date=date(2026, 6, 1), montant=Centimes(valeur=54900)),
            Versement(date=date(2026, 9, 1), montant=Centimes(valeur=54900)),
            Versement(date=date(2026,10, 1), montant = Centimes(valeur=18300)),
        ],
        "alerte_derniere_annee": True
    }

def test_internat():
    resultat = get_aide_handicap_moins_20ans(
        annee_demandee=2026,
        date_naissance= date(year=2009, month=9, day=12),
        date_fin_validite= date(year=2028, month=10, day=23),
        pourcentage_incapacite_permanente= 60,
        pourcentage_hors_internat= 70
    )

    assert str(resultat.value) == '128.1€'
    assert resultat.explanation == {
        "versements": [
            Versement(date=date(2026, 6, 1), montant=Centimes(valeur=38430)),
            Versement(date=date(2026, 9, 1), montant=Centimes(valeur=38430)),
            Versement(date=date(2026,12, 1), montant = Centimes(valeur=38430)),
            Versement(date=date(2027, 3, 1), montant=Centimes(valeur=38430))
        ],
        "alerte_derniere_annee": False
    }

def test_aeeh_ending():
    resultat = get_aide_handicap_moins_20ans(
        annee_demandee=2026,
        date_naissance=date(year=2009, month=9, day=12),
        date_fin_validite=date(year=2026, month=10, day=23),
        pourcentage_incapacite_permanente=60,
        pourcentage_hors_internat=70
    )

    assert str(resultat.value) == '128.1€'
    assert resultat.explanation == {
        "versements": [
            Versement(date=date(2026, 6, 1), montant=Centimes(valeur=38430)),
            Versement(date=date(2026, 9, 1), montant=Centimes(valeur=38430)),
            Versement(date=date(2026, 11, 1), montant=Centimes(valeur=25620)),
        ],
        "alerte_derniere_annee": False
    }

def test_handicap_inneligible():
    resultat = get_aide_handicap_moins_20ans(
        annee_demandee=2026,
        date_naissance=date(year=2016, month=9, day=12),
        date_fin_validite=date(year=2028, month=10, day=23),
        pourcentage_incapacite_permanente=30,
        pourcentage_hors_internat=70
    )

    assert str(resultat.value) == '0.0€'
    assert resultat.explanation == {
        "versements": [],
        "alerte_derniere_annee": False
    }
