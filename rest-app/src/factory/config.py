
import os

from src.schemes.settings import APISettings

class APIConfig:
    def __init__(self, host, port, is_reload):
        """
        Class to hold configuration settings for an API.

        Attributes:
            host (str): The host of the API.
            port (int): The port number of the API.
            is_reload (bool): Flag indicating whether hot reload is enabled.
        """
        self.host = host
        self.port = port
        self.is_reload = is_reload

    @classmethod
    def from_envvar(cls):
        """
        Initialize APIConfig with the provided host, port, and hot reload flag.

        Args:
            host (str): The host of the API.
            port (int): The port number of the API.
            is_reload (bool): Flag indicating whether hot reload is enabled.
        """
        
        config = APISettings(
            host=os.environ.get("API_HOST"),
            port=os.environ.get("API_PORT_IN"),
            is_reload=os.environ.get("IS_RELOAD", True)
        )
        
        return cls(host=config.host, port=config.port, is_reload=config.is_reload)
