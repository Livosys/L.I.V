from freshservice.ticket_client import list_tickets

def list_filtered(filters: dict):
    tickets = list_tickets() or []

    if not tickets:
        return []

    if "priority" in filters:
        tickets = [t for t in tickets if t.get("priority") == filters["priority"]]

    if filters.get("owner") == "none":
        tickets = [t for t in tickets if not t.get("responder_id")]

    if filters.get("sla") == "breached":
        tickets = [t for t in tickets if t.get("sla_breached") is True]

    return tickets

def count_filtered(filters: dict):
    return len(list_filtered(filters))
