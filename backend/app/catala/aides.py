from prestagri_catala.Personne import Personne
from prestagri_catala.catala_runtime import Money, Integer

def impot_revenu(montant) -> str:
    personne = Personne(Money(Integer(100000)), Integer(3))
    return str(personne)