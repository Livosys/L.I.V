from freshservice.client import (
    get_ticket,
    get_ticket_notes
)
from shix.mapper import map_ticket, html_to_text

def assemble_ticket(ticket_id: int) -> dict | None:
    raw = get_ticket(ticket_id)
    if not raw:
        return None

    ticket = map_ticket(raw)

    notes_raw = get_ticket_notes(ticket_id)
    notes = []

    for n in notes_raw.get("notes", []):
        notes.append({
            "id": n.get("id"),
            "author_id": n.get("user_id"),
            "private": n.get("private"),
            "body": html_to_text(n.get("body")),
            "created_at": n.get("created_at")
        })

    ticket["notes"] = notes
    return ticket
