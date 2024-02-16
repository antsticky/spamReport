from pydantic import BaseModel

class TicketStateUpdate(BaseModel):
    """
    Model for updating the state of a ticket.

    Attributes:
        ticketState (str): The new state of the ticket.
    """
    
    ticketState: str