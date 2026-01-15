import requests, os

BASE_URL = os.getenv("FRESHSERVICE_BASE_URL")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def add_note(ticket_id: int, text: str, private=True):
    r = requests.post(
        f"{BASE_URL}/tickets/{ticket_id}/notes",
        auth=(API_KEY, "X"),
        json={
            "body": text,
            "private": private
        }
    )
    r.raise_for_status()
    return r.json()
