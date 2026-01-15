import services.freshservice as fs
from services.audit import log

def propose_resolution(ticket_id: int, text: str, user: str):
    log(user, "propose_resolution", {"ticket_id": ticket_id})
    return {
        "ticket_id": ticket_id,
        "proposal": text,
        "status": "PROPOSED"
    }

def apply_resolution(ticket_id: int, text: str, user: str):
    fs.add_note(ticket_id, text)
    fs.resolve_ticket(ticket_id)
    log(user, "apply_resolution", {"ticket_id": ticket_id})
    return {
        "ticket_id": ticket_id,
        "status": "APPLIED"
    }
