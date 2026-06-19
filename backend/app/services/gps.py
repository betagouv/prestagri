from app.model import Trajet


def get_trajet(adresse_depart: str, adresse_arrivee: str) -> Trajet:
    print("TESSST")
    print(adresse_depart)
    return Trajet(30, 25)