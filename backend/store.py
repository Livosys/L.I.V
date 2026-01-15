import json

with open("/opt/shix/backend/data/synthetic_tickets.json") as f:
    TICKETS = json.load(f)

def list_tickets(limit=10, offset=0):
    return TICKETS[offset:offset+limit]

def get_ticket(tid: int):
    for t in TICKETS:
        if t["id"] == tid:
            return t
    return None
