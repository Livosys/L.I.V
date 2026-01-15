import os
import requests
from rag.embedder import embed
from rag.vector_db import add

BASE = os.getenv("FRESHSERVICE_DOMAIN")
KEY  = os.getenv("FRESHSERVICE_API_KEY")

if not BASE or not KEY:
    raise RuntimeError("Missing Freshservice env vars")

def auth():
    return (KEY, "X")

headers = {"Accept": "application/json"}

# 1. Fetch tickets
r = requests.get(
    f"{BASE}/api/v2/tickets",
    auth=auth(),
    headers=headers,
    timeout=30
)
r.raise_for_status()

tickets = r.json().get("tickets", [])

for t in tickets:
    ticket_id = t.get("id")

    # 2. Fetch notes
    notes_resp = requests.get(
        f"{BASE}/api/v2/tickets/{ticket_id}/notes",
        auth=auth(),
        headers=headers,
        timeout=30
    )
    notes = []
    if notes_resp.status_code == 200:
        notes = notes_resp.json().get("notes", [])

    # 3. Build knowledge text
    text = f"""
Ticket #{ticket_id}
Subject: {t.get('subject')}
Description: {t.get('description_text')}
Status: {t.get('status')}
Priority: {t.get('priority')}

Notes:
"""

    for n in notes:
        if not n.get("private"):
            text += f"- {n.get('body_text')}\n"

    # 4. Add to vector DB
    add(
        text.strip(),
        embed(text),
        source=f"ticket:{ticket_id}"
    )

print("TICKETS + NOTES INGEST OK")
