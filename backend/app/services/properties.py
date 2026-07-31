from typing import Any
import yaml
from pydantic import BaseModel
import os

class Properties (BaseModel):
    error_contact: str
    sentry_dsn: str
    dn_pilotage_token: str
    dn_demarche_id: str
    grist_pilotage_token: str
    grist_doc_id: str
    dn_instructeurice_id: str

    @classmethod
    def import_properties(cls):
        yaml_data = cls.get_yaml_prop()
        varenv_data = cls.get_var_env_prop()
        return cls(
            error_contact=yaml_data["error_contact"],
            sentry_dsn=varenv_data["sentry_dsn"],
            dn_pilotage_token=varenv_data["dn_pilotage_token"],
            dn_demarche_id=varenv_data["dn_demarche_id"],
            grist_pilotage_token=varenv_data["grist_pilotage_token"],
            grist_doc_id=varenv_data["grist_doc_id"],
            dn_instructeurice_id=varenv_data["dn_instructeurice_id"],
        )

    @staticmethod
    def get_yaml_prop() :
        with open("config.yml") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def get_var_env_prop():
        return {
            "sentry_dsn" : os.environ['SENTRY_DSN'],
            "dn_pilotage_token" : os.environ['DN_PILOTAGE_TOKEN'],
            "dn_demarche_id" : os.environ['DN_DEMARCHE_ID'],
            "grist_pilotage_token" : os.environ['GRIST_API_KEY'],
            "grist_doc_id" : os.environ['GRIST_DOC_ID'],
            "dn_instructeurice_id": os.environ['DN_INSTRUCTEURICE_ID'],

        }

properties = Properties.import_properties()
