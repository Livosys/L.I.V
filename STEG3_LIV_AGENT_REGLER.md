STEG 3 – L.I.V AGENT + INTENT-ROUTER (LÅSNING)

MÅL:
- Förutsägbart beteende
- Ingen hallucination
- All logik styrs i backend
- Frontend (Lovable) är dum renderare

=================================
1. L.I.V – GRUNDREGLER (MÅSTE GÄLLA ALLTID)
=================================

L.I.V FÅR:
✔ Läsa tickets
✔ Läsa KB
✔ Använda RAG
✔ Returnera strukturerad UI-data

L.I.V FÅR INTE:
❌ Skriva till Freshservice
❌ Ändra tickets
❌ Skapa tickets
❌ Gissa eller hitta på data

=================================
2. INTENT-ROUTER (SANNINGEN)
=================================

ALL user-input ska först klassificeras till INTENT.

TILLÅTNA INTENTS:

- LIST_TICKETS
- OPEN_TICKET
- LIST_KB
- OPEN_KB
- SEARCH_RAG
- SMALL_TALK
- UNKNOWN

INGA andra intents får existera.

=================================
3. CHAT ROUTER – KONTRAKT
=================================

FIL: /opt/shix/backend/routers/chat.py

ANSVAR:
- Ta emot text
- Avgöra intent
- Anropa RÄTT modul
- Aldrig själv hämta data

chat.py får ENDAST:
- intent-detection
- dispatch

=================================
4. DATA-FLÖDE (LÅST)
=================================

USER
 ↓
/api/chat
 ↓
INTENT
 ↓
[ tickets | kb | rag ]
 ↓
STRUKTURERAT SVAR
 ↓
Lovable UI

INGET ANNAT FLÖDE ÄR TILLÅTET.

=================================
5. RAG-REGLER (KRITISKT)
=================================

RAG används ENDAST när:
- intent == SEARCH_RAG
- eller fallback vid UNKNOWN

RAG FÅR:
✔ sammanfatta
✔ länka
✔ citera metadata

RAG FÅR INTE:
❌ hitta på svar
❌ svara utan källa

=================================
6. UI-KONTRAKT MOT LOVABLE
=================================

Backend returnerar ALLTID JSON med:
- answer (text)
- ui (list, cards, actions)

Lovable:
- renderar exakt
- ingen egen logik
- inga API-anrop förutom backend

=================================
7. FELHANTERING (OBLIGATORISK)
=================================

Vid fel:
- svara med text
- visa aldrig stacktrace
- returnera stabil JSON

=================================
8. EFTER STEG 3
=================================

SYSTEMET ÄR NU:
✔ Deterministiskt
✔ Produktionssäkert
✔ Utbyggbart (Steg 4 = MCP / Write-mode)

NÄSTA STEG:
STEG 4 – MCP + KONTROLLERAD WRITE-PIPELINE

