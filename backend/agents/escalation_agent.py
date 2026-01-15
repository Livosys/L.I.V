from backend.freshservice.writeback import add_note

def auto_escalate(ticket: dict):
    add_note(
        ticket["id"],
        "⚠️ SLA risk identifierad – ärendet har eskalerats automatiskt.",
        private=True
    )
    return "escalated"
