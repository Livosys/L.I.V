from datetime import datetime

def sla_assess(ticket: dict) -> dict:
    overdue = False
    due_by = ticket.get("due_by")
    if due_by:
        overdue = datetime.utcnow().isoformat() > due_by

    escalation = "none"
    if overdue or ticket.get("priority") in (1, 2):
        escalation = "immediate"

    return {
        "overdue": overdue,
        "escalation": escalation
    }
