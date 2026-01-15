import requests
import os

FRESH_BASE = os.getenv("FRESH_BASE_URL")
API_KEY   = os.getenv("FRESH_API_KEY")

def fetch_latest_tickets(limit=50):
    url = f"{FRESH_BASE}/api/v2/tickets?per_page={limit}"
    r = requests.get(url, auth=(API_KEY, "X"))
    r.raise_for_status()
    return r.json().get("tickets", [])
