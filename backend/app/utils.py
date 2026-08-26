import logging

logger = logging.getLogger(__name__)

def to_bool(str_bool : str) -> bool :
    return str_bool == "true"
