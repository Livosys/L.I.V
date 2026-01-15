import re
from services.freshservice import get_ticket, search_kb


def detect_intent(query: str) -> dict:
    q = query.lower()

    match = re.search(r"(ärende|ticket)\s*(\d+)", q)
    if match:
        return {
            "intent": "ticket_specific",
            "ticket_id": match.group(2)
        }

    if any(k in q for k in ["kb", "kunskapsbas", "artikel", "knowledge", "vpn"]):
        return {"intent": "kb_search"}

    return {"intent": "general_rag"}


def fetch_context(intent_data: dict, query: str) -> str:
    intent = intent_data["intent"]

    if intent == "ticket_specific":
        try:
            ticket = get_ticket(intent_data["ticket_id"])
        except Exception:
            return ""

        if not ticket:
            return ""

        return f"""
Ticket #{ticket.get('id')}
Subject: {ticket.get('subject')}
Status: {ticket.get('status')}
Description:
{ticket.get('description_text')}
""".strip()

    if intent == "kb_search":
        articles = search_kb(query)
        if not articles:
            return ""
        return "\n".join(
            f"- {a.get('title')}"
            for a in articles
        )

    return ""


def determine_confidence(intent: str, context: str) -> str:
    if intent == "kb_search" and context:
        return "Hög"
    if intent == "ticket_specific" and context:
        return "Medel"
    return "Låg"
