from services.freshservice import get_ticket, get_related_kb

def build_context(ticket_id: int) -> str:
    ticket = get_ticket(ticket_id)
    kb_articles = get_related_kb(ticket_id)

    context = f"""
TICKET
------
ID: {ticket.get('id')}
Subject: {ticket.get('subject')}
Description: {ticket.get('description_text')}
Status: {ticket.get('status')}

RELATED KB ARTICLES
-------------------
"""

    if not kb_articles:
        context += "None found.\n"
    else:
        for kb in kb_articles:
            context += f"- {kb.get('title')}\n"

    return context.strip()
