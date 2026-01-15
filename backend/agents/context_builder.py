def build_context_from_ticket(ticket: dict) -> str:
    """
    Gör ett semantiskt sammanhang av ett ärende
    """
    parts = []

    if ticket.get("subject"):
        parts.append(ticket["subject"])

    if ticket.get("description"):
        parts.append(ticket["description"])

    if ticket.get("category"):
        parts.append(ticket["category"])

    return " ".join(parts)
