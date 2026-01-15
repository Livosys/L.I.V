import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")
FRESHSERVICE_WORKSPACE_ID = os.getenv("FRESHSERVICE_WORKSPACE_ID", "2")

def add_note(ticket_id: int, body: str, private: bool = True):
    url = f"https://{FRESHSERVICE_DOMAIN}.freshservice.com/api/v2/tickets/{ticket_id}/notes"

    headers = {
        "Content-Type": "application/json",
        "X-Workspace-Id": str(FRESHSERVICE_WORKSPACE_ID)
    }

    payload = {
        "body": body,
        "private": private
    }

    r = requests.post(
        url,
        auth=(FRESHSERVICE_API_KEY, "X"),
        headers=headers,
        json=payload,
        timeout=15
    )

    if r.status_code not in (200, 201):
        raise Exception(f"Freshservice writeback failed: {r.status_code} {r.text}")

    return r.json()
