import os
from pymongo import MongoClient


from src.schemes.settings import MongoSettings


class MongoHandler:
    """
    Class to handle MongoDB connections.

    Attributes:
        client (pymongo.MongoClient): The MongoClient instance for the MongoDB connection.
    """

    def __init__(self, mongo_settings: MongoSettings):
        """
        Initialize MongoHandler with the provided MongoSettings.

        Args:
            mongo_settings (MongoSettings): An instance of MongoSettings containing MongoDB connection settings.
        """

        self.client = MongoClient(self._get_connection_str(mongo_settings))

    @staticmethod
    def _get_connection_str(mongo_settings: MongoSettings):
        """
        Construct MongoDB connection string from MongoSettings.

        Args:
            mongo_settings (MongoSettings): An instance of MongoSettings containing MongoDB connection settings.

        Returns:
            str: MongoDB connection string.
        """

        return f"mongodb://{mongo_settings.user}:{mongo_settings.password}@{mongo_settings.host}:{mongo_settings.port}"

    @classmethod
    def from_envvar(cls):
        """
        Construct MongoHandler object from environment variables.

        Returns:
            MongoHandler: An instance of MongoHandler initialized from environment variables.
        """

        mongo_settings = MongoSettings(
            port=os.environ.get("DB_PORT_IN"),
            host=os.environ.get("MONGO_HOST"),
            user=os.environ.get("MONGO_ROOT_USER"),
            password=os.environ.get("MONGO_ROOT_PWD"),
        )

        return cls(mongo_settings)
