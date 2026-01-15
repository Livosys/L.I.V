from fastapi import APIRouter
from shix.agentic import run_shix

router = APIRouter(
    prefix="/api/shix",
    tags=["SHIX AGENTIC"]
)

@router.get("/tickets/{ticket_id}")
def shix_ticket(ticket_id: int):
    result = run_shix(ticket_id)
    if not result:
        return {
            "error": "Ticket not found",
            "ticket_id": ticket_id
        }
    return result
