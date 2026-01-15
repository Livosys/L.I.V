from fastapi import APIRouter
from backend.freshservice.client import get_ticket
from backend.agents.problem_orchestrator import process

router = APIRouter(prefix="/api/problem", tags=["problem"])

@router.post("")
def problem(tickets: list[int]):
    data = [get_ticket(t).get("ticket", {}) for t in tickets]
    return process(data)
