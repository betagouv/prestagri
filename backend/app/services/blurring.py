import hashlib
import re

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
