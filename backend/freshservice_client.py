import os
import requests

BASE_URL = f"https://{os.getenv('FRESHSERVICE_DOMAIN')}/api/v2"
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def get_tickets():
    r = requests.get(
        f"{BASE_URL}/tickets",
        auth=(API_KEY, "X"),
        timeout=15,
    )
    return r.status_code, r.text
