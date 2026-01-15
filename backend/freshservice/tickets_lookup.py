import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")

BASE_URL = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/api/v2"

def get_tickets_by_email(email: str):
    url = f"{BASE_URL}/tickets"
    params = {
        "email": email,
        "per_page": 10
    }

    r = requests.get(
        url,
        auth=(FRESHSERVICE_API_KEY, "X"),
        params=params,
        timeout=20
    )

    # 🔒 Säker hantering
    if r.status_code != 200:
        return {
            "error": f"Freshservice error {r.status_code}",
            "tickets": []
        }

    data = r.json()
    tickets = data.get("tickets", [])

    safe_tickets = []
    for t in tickets:
        safe_tickets.append({
            "id": t.get("id"),
            "subject": t.get("subject", "No subject"),
            "status": t.get("status", "unknown")
        })

    return {
        "tickets": safe_tickets
    }
