import os
import requests
import logging

BASE_URL = os.getenv("FRESHSERVICE_BASE_URL")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

log = logging.getLogger("tickets")

def get_tickets(query: str = None, page: int = 1, per_page: int = 5):
    if not BASE_URL or not API_KEY:
        log.error("FRESHSERVICE_BASE_URL or API_KEY not set")
        return []

    url = f"{BASE_URL}/tickets"
    params = {
        "page": page,
        "per_page": per_page
    }

    try:
        r = requests.get(
            url,
            auth=(API_KEY, "X"),
            params=params,
            timeout=10
        )
        r.raise_for_status()

        tickets = r.json().get("tickets", [])

        if query:
            q = query.lower()
            tickets = [
                t for t in tickets
                if q in (t.get("subject") or "").lower()
            ]

        return tickets

    except Exception:
        log.exception("Ticket fetch failed")
        return []

def get_ticket(ticket_id: int):
    if not BASE_URL or not API_KEY:
        return None

    url = f"{BASE_URL}/tickets/{ticket_id}"

    try:
        r = requests.get(url, auth=(API_KEY, "X"), timeout=10)
        r.raise_for_status()
        return r.json().get("ticket")

    except Exception:
        log.exception("Ticket fetch failed")
        return None
