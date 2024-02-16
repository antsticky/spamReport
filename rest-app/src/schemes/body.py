from pydantic import BaseModel

class TicketStateUpdate(BaseModel):
    ticketState: str