def on_breach(ticket):
    return {
        "action": "escalate",
        "target": "L2",
        "ticket_id": ticket.get("id")
    }
