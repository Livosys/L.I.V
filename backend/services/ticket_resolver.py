from freshservice.ticket_client import get_my_open_tickets
from rag.semantic import semantic_search

def resolve_ticket(message: str, tenant: str):
    tickets = get_my_open_tickets(tenant=tenant, limit=5)

    if not tickets:
        return None

    texts = [
        f"{t['id']} {t.get('subject','')} {t.get('description_text','')}"
        for t in tickets
    ]

    match = semantic_search(
        query=message,
        documents=texts,
        top_k=1
    )

    if not match:
        return None

    idx = match[0]["index"]
    return tickets[idx]
