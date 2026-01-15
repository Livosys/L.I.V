from fastapi import APIRouter
from pydantic import BaseModel
from freshservice.tickets import get_ticket

router = APIRouter(prefix="/api/debug", tags=["debug"])

class Payload(BaseModel):
    ticket_id: int

@router.post("/freshservice")
def debug_ticket(p: Payload):
    return get_ticket(p.ticket_id)
