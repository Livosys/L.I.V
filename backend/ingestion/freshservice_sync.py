import os
import requests
from rag.pipeline import ingest_document

FRESHSERVICE_DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
FRESHSERVICE_API_KEY = os.getenv("FRESHSERVICE_API_KEY")

def fetch_all_tickets():
    if not FRESHSERVICE_DOMAIN or not FRESHSERVICE_API_KEY:
        print("❌ Missing Freshservice config in environment")
        return []

    all_tickets = []
    page = 1

    while True:
        url = f"https://{FRESHSERVICE_DOMAIN}/api/v2/tickets?page={page}&per_page=50"
        response = requests.get(url, auth=(FRESHSERVICE_API_KEY, "X"))

        if response.status_code != 200:
            print("❌ Freshservice API error:", response.text)
            break

        data = response.json()

        if "tickets" not in data or len(data["tickets"]) == 0:
            break

        all_tickets.extend(data["tickets"])
        page += 1

    print(f"✅ Retrieved {len(all_tickets)} tickets from Freshservice")
    return all_tickets


def format_ticket_for_rag(ticket):
    subject = ticket.get("subject", "[No subject]")
    description = ticket.get("description_text", "[No description]")

    plaintext = (
        f"Subject: {subject}\n"
        f"Priority: {ticket.get('priority')}\n"
        f"Status: {ticket.get('status')}\n"
        f"Requester: {ticket.get('requester_id')}\n"
        f"Description:\n{description}"
    )

    metadata = {
        "source": "freshservice_ticket",
        "ticket_id": ticket.get("id")
    }

    return plaintext, metadata


def ingest_all_freshservice_tickets():
    tickets = fetch_all_tickets()

    count = 0
    for t in tickets:
        text, metadata = format_ticket_for_rag(t)
        ingest_document(text, source_type="freshservice", metadata=metadata)
        count += 1

    return {"ingested": count}
