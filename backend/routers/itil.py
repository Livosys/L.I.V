from fastapi import APIRouter
from backend.freshservice.client import get_ticket
from backend.agents.change_agent import propose_change
from backend.agents.problem_agent import link_problem

router = APIRouter(prefix="/api/itil", tags=["itil"])

@router.post("/change/{ticket_id}")
def change(ticket_id:int):
    t = get_ticket(ticket_id).get("ticket",{})
    return {"status": propose_change(t)}

@router.post("/problem/{ticket_id}")
def problem(ticket_id:int):
    t = get_ticket(ticket_id).get("ticket",{})
    return {"status": link_problem(t)}
