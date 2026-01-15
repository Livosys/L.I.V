STEG 2 – LÅST ARKITEKTUR (SHIX)

MÅL:
- Ingen loop
- En entrypoint
- Routers monteras exakt en gång
- Systemd pekar på rätt app
- Stabil grund för RAG + MCP

=================================
1. ENTRYPOINT (ENDA FIL SOM UVICORN KÖR)
=================================

FIL: /opt/shix/backend/shix_entrypoint.py

INNEHÅLL (SKA SE UT EXAKT SÅ HÄR):

from fastapi import FastAPI
from routers.chat import router as chat_router
from routers.kb import router as kb_router
from routers.tickets import router as tickets_router
from routers.rag import router as rag_router

app = FastAPI()

@app.get("/")
def root():
    return {"entrypoint": "OK"}

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/debug")
def debug():
    return {"debug": "OK"}

app.include_router(chat_router, prefix="/api")
app.include_router(kb_router, prefix="/api")
app.include_router(tickets_router, prefix="/api")
app.include_router(rag_router, prefix="/api")

=================================
2. ROUTERS-STRUKTUR (KRAV)
=================================

/opt/shix/backend/routers/
  ├── __init__.py   (MÅSTE FINNAS)
  ├── chat.py
  ├── kb.py
  ├── tickets.py
  └── rag.py

VARJE router-fil SKA INNEHÅLLA:
- router = APIRouter()
- INGA app = FastAPI()

=================================
3. SYSTEMD (SANNINGEN)
=================================

FIL: /etc/systemd/system/shix-backend.service

ExecStart SKA PEKA PÅ:
uvicorn shix_entrypoint:app

INGET main.py
INGET auto-reload
INGET extra magic

=================================
4. FÖRBUD (ABSOLUT)
=================================

❌ app = FastAPI() i routers
❌ include_router i flera filer
❌ uvicorn som pekar på fel modul
❌ cirkulära imports
❌ reload=True i produktion

=================================
5. EFTER STEG 2
=================================

NÄR DETTA ÄR KLART:
- /           → OK
- /health     → OK
- /debug      → OK
- /api/chat   → FUNKAR
- /api/kb     → FUNKAR
- /api/tickets → FUNKAR
- /api/rag    → FUNKAR

DETTA ÄR BASEN.
INGET MER SKA ÄNDRAS HÄR.

NÄSTA STEG:
STEG 3 – L.I.V AGENT-REGLER + INTENT-ROUTER (LÅSNING)

