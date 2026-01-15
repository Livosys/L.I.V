import requests
import os
from ingestion.ingest import ingest_text

FRESH_BASE = os.getenv("FRESH_BASE")
FRESH_API_KEY = os.getenv("FRESH_API_KEY")

def fetch_tickets(limit=50):
    url = f"https://{FRESH_BASE}.freshservice.com/api/v2/tickets?per_page={limit}"

    r = requests.get(url, auth=(FRESH_API_KEY, "X"))
    if r.status_code != 200:
        raise Exception(f"Freshservice error: {r.text}")

    data = r.json()
    return data.get("tickets", [])

def ingest_ticket(ticket):
    ticket_id = ticket["id"]
    subject = ticket.get("subject", "")
    desc = ticket.get("description_text", "")
    status = ticket.get("status")
    priority = ticket.get("priority")

    text = f"""
Ticket ID: {ticket_id}
Subject: {subject}
Description: {desc}
Status: {status}
Priority: {priority}
"""

    return ingest_text(text)

def ingest_all_tickets():
    tickets = fetch_tickets(100)
    ingested = []
    for t in tickets:
        doc = ingest_ticket(t)
        ingested.append(doc)
    return ingested
