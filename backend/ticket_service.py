import json
from pathlib import Path

DATA = Path("/opt/shix/data/synthetic/tickets.json")

def list_tickets(filters=None):
    tickets = json.loads(DATA.read_text())

    if not filters:
        return tickets

    if filters.get("keyword"):
        tickets = [
            t for t in tickets
            if filters["keyword"].lower() in
            (t["subject"] + t["description"]).lower()
        ]

    if filters.get("status"):
        tickets = [t for t in tickets if t["status"] == filters["status"]]

    return tickets

def open_ticket(ticket_id: int):
    for t in json.loads(DATA.read_text()):
        if t["id"] == ticket_id:
            return t
    return None

def count_tickets():
    return len(json.loads(DATA.read_text()))
