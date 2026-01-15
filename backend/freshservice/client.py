import requests
import os

BASE_URL = "https://livosys.freshservice.com/api/v2"
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def get_ticket(ticket_id: int):
    r = requests.get(
        f"{BASE_URL}/tickets/{ticket_id}",
        auth=(API_KEY, "X")
    )
    r.raise_for_status()
    t = r.json()

    return {
        "id": t["id"],
        "subject": t["subject"],
        "status": t["status"],
        "priority": t["priority"]
    }
