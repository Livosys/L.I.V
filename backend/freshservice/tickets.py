import os
import requests

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")
FRESHSERVICE_WORKSPACE_ID = os.getenv("FRESHSERVICE_WORKSPACE_ID")

def get_my_tickets():
    """
    Read-only placeholder.
    Returns an empty list if Freshservice is not reachable.
    Safe for production startup.
    """
    if not FRESHSERVICE_DOMAIN or not FRESHSERVICE_API_KEY:
        return []

    url = f"https://{FRESHSERVICE_DOMAIN}/api/v2/tickets"
    try:
        r = requests.get(
            url,
            auth=(FRESHSERVICE_API_KEY, "X"),
            timeout=10
        )
        if r.status_code != 200:
            return []
        return r.json().get("tickets", [])
    except Exception:
        return []
