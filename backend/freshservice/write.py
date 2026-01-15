import requests

# ✅ ABSOLUT IMPORT (VIKTIGT)
from backend.freshservice.client import (
    get_base_url,
    get_auth,
    get_headers,
)

def add_ticket_note(ticket_id: int, body: str, private: bool = True):
    payload = {
        "body": body,
        "private": private
    }

    r = requests.post(
        f"{get_base_url()}/tickets/{ticket_id}/notes",
        auth=get_auth(),
        headers=get_headers(),
        json=payload,
        timeout=15
    )

    if r.status_code >= 400:
        raise RuntimeError(f"Freshservice error {r.status_code}: {r.text}")

    return r.json()
