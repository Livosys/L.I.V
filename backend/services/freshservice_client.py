import os
import requests

API_KEY = os.getenv("FRESHSERVICE_API_KEY")
DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")

BASE = f"https://{DOMAIN}.freshservice.com/api/v2"

def _headers():
    return {"Content-Type": "application/json"}

def list_tickets_live():
    r = requests.get(
        f"{BASE}/tickets",
        auth=(API_KEY, "X"),
        headers=_headers(),
        params={"per_page": 5}
    )
    r.raise_for_status()
    data = r.json().get("tickets", [])

    return {
        "mode": "live",
        "tickets": [
            {
                "id": t["id"],
                "subject": t["subject"],
                "status": t["status"],
                "priority": t["priority"],
                "updated": t["updated_at"]
            }
            for t in data
        ]
    }

def get_ticket_by_id_live(ticket_id: str):
    r = requests.get(
        f"{BASE}/tickets/{ticket_id}",
        auth=(API_KEY, "X"),
        headers=_headers()
    )
    r.raise_for_status()
    t = r.json()["ticket"]

    return {
        "mode": "live",
        "ticket": {
            "id": t["id"],
            "subject": t["subject"],
            "status": t["status"],
            "priority": t["priority"],
            "description": t.get("description_text"),
            "updated": t["updated_at"]
        }
    }
