from catala.generated.ImpotSimple import CalculImpotRevenuIn,CalculImpotRevenu, calcul_impot_revenu
from catala.generated.catala_runtime import Money, Integer

def impot_revenu(montant) -> int:
    input = CalculImpotRevenuIn(Money(Integer(1000)))
    result: CalculImpotRevenu = calcul_impot_revenu(input)
    return int(result.impot_revenu.value.value)