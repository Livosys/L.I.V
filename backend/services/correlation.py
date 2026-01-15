from freshservice.ticket_client import get_my_open_tickets

def correlate_incidents(ticket: dict, tenant: str):
    category = ticket.get("category")
    subject = ticket.get("subject", "").lower()

    related = []
    tickets = get_my_open_tickets(tenant=tenant, limit=20)

    for t in tickets:
        if t["id"] == ticket["id"]:
            continue

        if t.get("category") == category:
            related.append(t)
        elif any(w in t.get("subject","").lower() for w in subject.split()):
            related.append(t)

    return related[:5]
