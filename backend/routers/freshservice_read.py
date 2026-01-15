from fastapi import APIRouter
from freshservice.client import (
    get_tickets,
    get_ticket,
    get_ticket_notes
)

router = APIRouter(
    prefix="/api/freshservice",
    tags=["Freshservice READ"]
)

@router.get("/tickets")
def tickets():
    return get_tickets()

@router.get("/tickets/{ticket_id}")
def ticket(ticket_id: int):
    data = get_ticket(ticket_id)
    if data is None:
        return {
            "error": "Ticket not found",
            "ticket_id": ticket_id
        }
    return data

@router.get("/tickets/{ticket_id}/notes")
def notes(ticket_id: int):
    data = get_ticket_notes(ticket_id)

    # 🔒 ABSOLUTT SKYDD – aldrig 500
    if data is None:
        return {
            "ticket_id": ticket_id,
            "notes": []
        }

    if "notes" not in data:
        return {
            "ticket_id": ticket_id,
            "notes": []
        }

    return data
