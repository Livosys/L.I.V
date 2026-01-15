import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def add_note(ticket_id: int, body: str, private: bool = True):
    url = f"https://{FRESHSERVICE_DOMAIN}/api/v2/tickets/{ticket_id}/notes"

    payload = {
        "body": body,
        "private": private
    }

    r = requests.post(
        url,
        auth=(FRESHSERVICE_API_KEY, "X"),
        json=payload,
        timeout=15
    )

    if not r.ok:
        raise Exception(f"Freshservice error: {r.status_code} {r.text}")

    return r.json()
