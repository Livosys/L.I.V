import requests
import os

DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")
BASE = f"https://{DOMAIN}.freshservice.com/api/v2"

def get_agent_by_email(email: str):
    r = requests.get(
        f"{BASE}/agents",
        auth=(API_KEY, "X"),
        timeout=15
    )
    r.raise_for_status()
    agents = r.json().get("agents", [])
    for a in agents:
        if a.get("email") == email:
            return a["id"]
    return None
