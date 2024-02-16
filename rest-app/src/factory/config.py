
import os

from src.schemes.settings import APISettings

class APIConfig:
    def __init__(self, host, port, is_reload):
        self.host = host
        self.port = port
        self.is_reload = is_reload

    @classmethod
    def from_envvar(cls):
        config = APISettings(
            host=os.environ.get("API_HOST"),
            port=os.environ.get("API_PORT_IN"),
            is_reload=os.environ.get("IS_RELOAD", True)
        )
        
        return cls(host=config.host, port=config.port, is_reload=config.is_reload)
