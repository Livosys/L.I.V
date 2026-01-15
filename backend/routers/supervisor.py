from fastapi import APIRouter
from agents.supervisor import supervisor_run

router = APIRouter(prefix="/api/supervisor", tags=["supervisor"])

@router.post("/run")
def run_supervisor(payload: dict):
    return supervisor_run(
        ticket_id=payload.get("ticket_id"),
        goal=payload.get("goal")
    )
