from app.catala.aides import get_catala_quotient_familial
from app.model import Response, Menage, Centimes


def get_quotient_familial(menage: Menage) -> Response[Centimes]:
    return get_catala_quotient_familial(menage)