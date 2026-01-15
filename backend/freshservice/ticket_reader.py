import requests
import os

BASE_URL = os.getenv("FRESHSERVICE_BASE_URL")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def fetch_tickets(limit=50):
    r = requests.get(
        f"{BASE_URL}/tickets",
        auth=(API_KEY, "X"),
        params={"per_page": limit}
    )
    r.raise_for_status()
    return r.json().get("tickets", [])
