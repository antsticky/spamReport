from pydantic import BaseModel


class MongoSettings(BaseModel):
    """
    Model for MongoDB connection settings.

    Attributes:
        port (int): The port number of the MongoDB server.
        host (str): The hostname or IP address of the MongoDB server.
        user (str): The username for authentication to the MongoDB server.
        password (str): The password for authentication to the MongoDB server.
    """

    port: int
    host: str
    user: str
    password: str

class APISettings(BaseModel):
    """
    Model for API settings.

    Attributes:
        host (str): The hostname or IP address of the API server.
        port (int): The port number of the API server.
        is_reload (bool): Flag indicating whether hot reload is enabled for the API server.
    """
    
    host: str
    port: int
    is_reload: bool 