from app.catala.aides import get_catala_quotient_familial
from app.model import Response, Famille, Centimes


def get_quotient_familial(famille: Famille) -> Response[Centimes]:
    return get_catala_quotient_familial(famille)