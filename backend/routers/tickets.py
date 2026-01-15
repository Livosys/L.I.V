from fastapi import APIRouter
from freshservice.ticket_client import list_tickets as fs_list_tickets
from freshservice.ticket_client import get_ticket

router = APIRouter()

def list_tickets():
    tickets = fs_list_tickets()
    items = []

    for t in tickets:
        items.append({
            "label": f"#{t['id']} {t['subject']}",
            "action": {
                "type": "chat",
                "value": str(t["id"])
            }
        })

    return {
        "answer": "Här är dina ärenden",
        "ui": {
            "type": "list",
            "items": items
        }
    }

def open_ticket(ticket_id: str):
    t = get_ticket(ticket_id)

    return {
        "answer": f"Ärende #{t['id']}",
        "ui": {
            "type": "text",
            "value": t.get("description_text", "")
        }
    }
