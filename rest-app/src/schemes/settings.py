from pydantic import BaseModel


class MongoSettings(BaseModel):
    port: int
    host: str
    user: str
    password: str

class APISettings(BaseModel):
    host: str
    port: int
    is_reload: bool 