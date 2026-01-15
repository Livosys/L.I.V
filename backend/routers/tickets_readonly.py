from fastapi import APIRouter
from freshservice.tickets import get_my_tickets_safe
from freshservice.agents import get_agent_name

router = APIRouter(
    prefix="/api/tickets-readonly",
    tags=["tickets-readonly"]
)

@router.get("")
def my_tickets():
    tickets = get_my_tickets_safe()

    simplified = []
    for t in tickets:
        owner_id = t.get("responder_id") or t.get("assigned_to")
        simplified.append({
            "id": t.get("id"),
            "subject": t.get("subject"),
            "status": t.get("status"),
            "owner": get_agent_name(owner_id)
        })

    return {
        "count": len(simplified),
        "tickets": simplified
    }
