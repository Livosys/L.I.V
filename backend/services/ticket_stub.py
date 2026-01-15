TICKETS = [
    {
        "id": "INC-1023",
        "subject": "VPN fungerar inte",
        "status": "Öppet",
        "priority": "Hög",
        "description": "VPN-klienten tappar anslutning efter inloggning.",
        "updated": "2026-01-02"
    },
    {
        "id": "REQ-884",
        "subject": "Åtkomst till ekonomisystem",
        "status": "Väntar",
        "priority": "Medium",
        "description": "Behöver behörighet till ekonomisystemet.",
        "updated": "2026-01-01"
    }
]

def list_tickets_stub():
    return {
        "mode": "pre-production",
        "tickets": TICKETS
    }

def get_ticket_by_id_stub(ticket_id: str):
    for t in TICKETS:
        if t["id"].lower() == ticket_id.lower():
            return {
                "mode": "pre-production",
                "ticket": t
            }
    return {
        "error": "not_found",
        "message": f"Inget ärende hittades med ID {ticket_id}"
    }
