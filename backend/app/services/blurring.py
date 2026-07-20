def blur_birthdate(birthdate: str) -> str :
    year = birthdate[-4:]
    decade = year[:3] + "0"
    return decade
