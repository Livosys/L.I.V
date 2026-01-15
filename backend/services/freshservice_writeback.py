import os
import requests

BASE_URL = f"https://{os.getenv('FRESHSERVICE_DOMAIN')}/api/v2"
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def add_note(ticket_id: int, text: str, private: bool = True):
    if not API_KEY or not BASE_URL:
        raise RuntimeError("Freshservice ENV missing")

    r = requests.post(
        f"{BASE_URL}/tickets/{ticket_id}/notes",
        auth=(API_KEY, "X"),
        json={"body": text, "private": private},
        headers={"Content-Type": "application/json"}
    )
    r.raise_for_status()
    return r.json()
