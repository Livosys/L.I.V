import os
import requests

FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")
FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")

BASE_URL = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/api/v2"

def _auth():
    return (FRESHSERVICE_API_KEY, "X")

def list_tickets(query=None):
    r = requests.get(
        f"{BASE_URL}/tickets",
        auth=_auth(),
        timeout=10
    )
    r.raise_for_status()
    return {"tickets": r.json().get("tickets", [])}

def get_ticket_by_id(ticket_id):
    r = requests.get(
        f"{BASE_URL}/tickets/{ticket_id}",
        auth=_auth(),
        timeout=10
    )
    if r.status_code != 200:
        return {}
    return {"ticket": r.json().get("ticket")}

def search_tickets(query: str):
    data = list_tickets()
    tickets = data.get("tickets", [])

    q = query.lower()
    matched = [
        t for t in tickets
        if q in (
            (t.get("subject","") + " " + t.get("description","")).lower()
        )
    ]

    return {"tickets": matched}
