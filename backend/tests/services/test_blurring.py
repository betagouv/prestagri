from app.services.blurring import blur_birthdate

def test_blurring_age():
    assert blur_birthdate("12 juin 1987") == "1980"
