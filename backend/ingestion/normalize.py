def normalize_ticket(ticket: dict) -> str:
    subject = ticket.get("subject", "")
    desc    = ticket.get("description_text", "") or ticket.get("description", "")
    priority = ticket.get("priority", "")
    status   = ticket.get("status", "")

    return f"Subject: {subject}\nPriority: {priority}\nStatus: {status}\n\nDescription:\n{desc}"
