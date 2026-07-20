def blur_birthdate(birthdate: str) -> str :
    year = birthdate[-4]
    decade = year[:-1] + "0"
    return decade
