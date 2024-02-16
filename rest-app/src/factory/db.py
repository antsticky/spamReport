import os
from pymongo import MongoClient


from src.schemes.settings import MongoSettings

class MongoHandler:
    def __init__(self, mongo_settings: MongoSettings):
        self.client = MongoClient(self._get_connection_str(mongo_settings))

    @staticmethod
    def _get_connection_str(mongo_settings: MongoSettings):
        return f"mongodb://{mongo_settings.user}:{mongo_settings.password}@{mongo_settings.host}:{mongo_settings.port}"

    @classmethod
    def from_envvar(cls):
        mongo_settings = MongoSettings(
            port=os.environ.get("DB_PORT_IN"),
            host=os.environ.get("MONGO_HOST"),
            user=os.environ.get("MONGO_ROOT_USER"),
            password=os.environ.get("MONGO_ROOT_PWD"),
        )

        return cls(mongo_settings)