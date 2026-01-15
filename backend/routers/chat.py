from fastapi import APIRouter
from typing import Dict

from routers.tickets import list_tickets, open_ticket
from routers.kb import list_kb, open_kb
from routers.rag import search_rag

router = APIRouter()

def classify_intent(message: str) -> str:
    m = message.lower().strip()

    if m in {"visa ärenden", "lista ärenden", "ärenden"}:
        return "LIST_TICKETS"
    if m.isdigit():
        return "OPEN_TICKET"
    if m in {"visa kb", "kunskapsbas", "kb"}:
        return "LIST_KB"
    if m.startswith("kb "):
        return "OPEN_KB"
    if len(m) >= 3:
        return "SEARCH_RAG"

    return "UNKNOWN"


@router.post("/chat")
def chat(payload: Dict):
    message = payload.get("message", "")
    intent = classify_intent(message)

    if intent == "LIST_TICKETS":
        return list_tickets()

    if intent == "OPEN_TICKET":
        return open_ticket(message)

    if intent == "LIST_KB":
        return list_kb()

    if intent == "OPEN_KB":
        return open_kb(message)

    if intent == "SEARCH_RAG":
        return search_rag(message)

    return {
        "answer": "Jag förstod inte frågan.",
        "ui": None
    }
