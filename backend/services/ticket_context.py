from freshservice.client import get_ticket, get_ticket_notes


def load_ticket_context(ticket_id: int) -> dict:
    ticket = get_ticket(ticket_id)

    # Om Freshservice blockerar → kör utan notes
    notes = []
    if ticket.get("error") != "forbidden":
        notes = get_ticket_notes(ticket_id)

    return {
        "ticket": ticket,
        "notes": notes
    }
