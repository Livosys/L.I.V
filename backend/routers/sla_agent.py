from fastapi import APIRouter
from freshservice_client import get_ticket

router = APIRouter(prefix="/api/sla", tags=["sla"])

@router.get("/risk/{ticket_id}")
def sla_risk(ticket_id: int):
    ticket = get_ticket(ticket_id)

    priority = ticket.get("priority")
    status = ticket.get("status")

    risk = "low"
    if priority == 1 and status != 5:
        risk = "high"

    return {
        "ticket_id": ticket_id,
        "risk": risk
    }
