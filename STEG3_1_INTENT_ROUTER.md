STEG 3.1 – IMPLEMENTERA INTENT-ROUTER (KOD)

MÅL:
- Deterministisk intent-klassificering
- Ingen loop
- En väg per intent
- Inga side-effects

=================================
KOD – chat router (ERSÄTT FIL)
=================================

FIL: /opt/shix/backend/routers/chat.py

INNEHÅLL:

from fastapi import APIRouter
from typing import Dict

router = APIRouter()

ALLOWED_INTENTS = {
    "LIST_TICKETS",
    "OPEN_TICKET",
    "LIST_KB",
    "OPEN_KB",
    "SEARCH_RAG",
    "SMALL_TALK",
    "UNKNOWN",
}

def classify_intent(message: str) -> str:
    m = message.lower().strip()

    if m in {"visa ärenden", "lista ärenden", "ärenden"}:
        return "LIST_TICKETS"
    if m.startswith("visa ") and m.split(" ")[1].isdigit():
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

    if intent not in ALLOWED_INTENTS:
        intent = "UNKNOWN"

    return {
        "intent": intent,
        "message": message
    }

=================================
NÄSTA STEG (AUTOMATISKT EFTER DETTA)
=================================

STEG 3.2:
- Koppla varje intent till RÄTT modul
- LIST_TICKETS → tickets client
- OPEN_TICKET  → ticket detail
- SEARCH_RAG   → semantic search
- INGA svar i chat.py

=================================
VERIFIERING (KÖRS EFTER DENNA PROMPT)
=================================

Skapa verifieringsscript:

cat << 'EOF' > /tmp/verify_step3_1.sh
curl -s -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"visa ärenden"}'
echo
curl -s -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"4"}'
echo
curl -s -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"vpn"}'
