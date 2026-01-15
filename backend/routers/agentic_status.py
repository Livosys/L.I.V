from fastapi import APIRouter
from services.agentic_loop import AgenticLoop

router = APIRouter(prefix="/api/agentic", tags=["agentic"])
agent = AgenticLoop()

@router.get("/{ticket_id}")
def status(ticket_id: int):
    return agent.run({"ticket_id": ticket_id})
