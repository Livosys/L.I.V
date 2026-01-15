from fastapi import APIRouter
from .tickets import list_tickets
from .kb import list_kb

def handle_intent(intent: str):
    if intent == "LIST_TICKETS":
        return list_tickets()
    if intent == "LIST_KB":
        return list_kb()
    return {"error": "UNKNOWN_INTENT"}
