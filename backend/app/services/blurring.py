import hashlib

def blur_birthdate(birthdate: str) -> str :
    year = birthdate[-4:]
    decade = year[:-1] + "0"
    return decade

def blur_id(_id:str) -> str :
    hash_object = hashlib.sha256(_id.encode())
    return hash_object.hexdigest()
