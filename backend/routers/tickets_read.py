from fastapi import APIRouter, HTTPException
import requests
from backend.freshservice.client import (
    get_base_url,
    get_auth,
    get_headers
)

router = APIRouter(
    prefix="/api/tickets",
    tags=["tickets"]
)

@router.get("/{ticket_id}")
def get_ticket(ticket_id: int):
    r = requests.get(
        f"{get_base_url()}/tickets/{ticket_id}",
        auth=get_auth(),
        headers=get_headers(),
        timeout=15
    )

    if r.status_code == 404:
        raise HTTPException(404, "Ticket not found")

    if r.status_code >= 400:
        raise HTTPException(502, r.text)

    return r.json()
