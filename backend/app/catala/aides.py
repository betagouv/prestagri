from .generated.Personne import Personne
from .generated.catala_runtime import Money, Integer

def impot_revenu(montant) -> str:
    personne = Personne(Money(Integer(100000)), Integer(3))
    return str(personne)