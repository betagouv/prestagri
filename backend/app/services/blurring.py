import hashlib
import re
from datetime import datetime

from app.model import DossierState


def blur_birthdate(birthdate: str) -> str :
    year = birthdate[-4:]
    decade = year[:-1] + "0"
    return decade

def blur_id(_id:str) -> str :
    hash_object = hashlib.sha256(_id.encode())
    return hash_object.hexdigest()

def get_assigned_gender(securite_sociale: str) -> str:
    identifier = securite_sociale[0]
    if identifier == "1":
        return "H"
    elif identifier == "2":
        return "F"
    return "N/A"

def blur_address(address: str) -> str:
    search = re.search(r'[0-9]{5}', address) # get postal code in address
    return search.group()[:2] if search else "00" # get department number

def blur_date_to_month(date: datetime) -> int:
    return date.month

def blur_date_to_year(date: datetime) -> int:
    return date.year

def blur_date_as_duration(start: datetime | None, end: datetime | None, state: DossierState) -> int | None:
    if state in [DossierState.INSTRUCTION, DossierState.CONSTRUCTION] or start is None or end is None :
        return None
    else:
        return (end - start).days

def blur_money_by_rounding(amount: float, base: int) -> int :
    return base * round(amount/base)
