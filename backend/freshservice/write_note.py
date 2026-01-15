import os
import requests

BASE_URL = os.getenv("FRESHSERVICE_BASE_URL")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def add_note(ticket_id: int, text: str):
    url = f"{BASE_URL}/tickets/{ticket_id}/notes"
    payload = {
        "body": text,
        "private": True
    }

    r = requests.post(
        url,
        auth=(API_KEY, "X"),
        json=payload,
        timeout=10
    )
    r.raise_for_status()
    return True
