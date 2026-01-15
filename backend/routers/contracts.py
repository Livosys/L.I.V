from pydantic import BaseModel
from typing import Optional, Dict, Any


class TicketContext(BaseModel):
    ticket: Dict[str, Any]
    notes: list


class RagPayload(BaseModel):
    query: str
    ticket_id: Optional[int] = None
