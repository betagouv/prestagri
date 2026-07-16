from typing import Any
import yaml
from pydantic import BaseModel

class Properties (BaseModel):
    error_contact: str

    @classmethod
    def import_properties(cls):
        yaml_data = cls.get_yaml_prop()
        varenv_data = cls.get_var_env_prop()
        return cls(error_contact=yaml_data["error_contact"])

    @staticmethod
    def get_yaml_prop() :
        with open("config.yml") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def get_var_env_prop():
        return {"info": "no env var"}
