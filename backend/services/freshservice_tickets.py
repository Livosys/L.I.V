import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")

BASE_URL = f"https://{FRESHSERVICE_DOMAIN}/api/v2"

def get_tickets_for_requester(email: str):
    url = f"{BASE_URL}/tickets"
    params = {
        "email": email,
        "include": "requester"
    }

    r = requests.get(
        url,
        params=params,
        auth=(FRESHSERVICE_API_KEY, "X"),
        timeout=10
    )

    if not r.ok:
        raise RuntimeError(f"Freshservice error {r.status_code}: {r.text}")

    return r.json().get("tickets", [])
