import requests, os

API_KEY = os.getenv("FRESHSERVICE_API_KEY")
DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
BASE = f"https://{DOMAIN}.freshservice.com/api/v2"

def update_ticket(ticket_id: int, payload: dict):
    url = f"{BASE}/tickets/{ticket_id}"
    r = requests.put(
        url,
        auth=(API_KEY, "X"),
        json=payload,
        timeout=10
    )
    r.raise_for_status()
    return r.json()
