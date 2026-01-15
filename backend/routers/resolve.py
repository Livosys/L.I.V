from fastapi import APIRouter
from backend.freshservice.client import get_ticket
from backend.agents.sla_agent import sla_risk
from backend.agents.resolution_agent import auto_resolve

router = APIRouter(prefix="/api/resolve", tags=["resolve"])

@router.post("/{ticket_id}")
def resolve(ticket_id: int):
    ticket = get_ticket(ticket_id).get("ticket", {})
    if sla_risk(ticket) == "ok":
        return {"status": auto_resolve(ticket)}
    return {"status": "manual_review"}
