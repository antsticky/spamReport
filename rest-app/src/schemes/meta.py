from datetime import datetime
from pydantic import BaseModel

from src.misc.date import human_readable_time_diff


class ApiMetadata(BaseModel):
    """
    Model for metadata about the API application.

    Attributes:
        start_date (datetime): The start date of the API application.
        human_readable_uptime (str): The human readable uptime of the API application.
    """

    start_date: datetime = datetime.now()

    @property
    def human_readable_uptime(self) -> str:
        return human_readable_time_diff(self.start_date, datetime.now())
