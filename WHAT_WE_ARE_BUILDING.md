VAD VI BYGGER JUST NU

KORT SVAR:
JA — vi bygger en AGENT.
Men inte en fri LLM-agent.
Detta är en KONTROLLERAD PRODUKTIONSAGENT.

=================================
VAD TYP AV AGENT
=================================

Typ:
- Deterministisk backend-agent
- Intent-styrd
- Regelbaserad orkestrering
- RAG-förstärkt vid behov

NAMN I SYSTEMET:
- L.I.V

=================================
VAD AGENTEN GÖR
=================================

Agenten:
- Tar emot naturligt språk
- Klassificerar INTENT
- Kör exakt en tillåten åtgärd
- Returnerar strukturerat svar till UI

Agenten TÄNKER INTE FRITT.
Den ORKESTRERAR.

=================================
VAD DEN INTE ÄR
=================================

❌ Inte AutoGPT
❌ Inte tool-loopande
❌ Inte självskrivande
❌ Inte hallucinerande

=================================
ARKITEKTURELL MODELL
=================================

USER
 ↓
/api/chat
 ↓
INTENT-ROUTER  ← (AGENTENS KÄRNA)
 ↓
[ tickets | kb | rag ]
 ↓
STRUCTURED RESPONSE
 ↓
Lovable UI

=================================
VARFÖR VI GÖR DETTA NU
=================================

Detta är NÖDVÄNDIGT innan:
- MCP
- Write-mode
- Autonoma workflows
- Multi-agent

Utan detta:
- kaos
- loopar
- datakorruption

=================================
NÄSTA STEG I PROJEKTET
=================================

STEG 3.1:
- Implementera INTENT-ROUTER i chat.py
- Låsa tillåtna intents i kod
- En funktion per intent

=================================
VERIFIERING (EFTER STEG 3.1)
=================================

Skapa testscript:
- Skicka olika meddelanden
- Se att rätt intent triggas
- Ingen RAG när det inte behövs

