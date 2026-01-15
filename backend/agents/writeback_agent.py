import os
from audit.logger import log_event
from backend.freshservice.ticket_client import add_note_to_ticket

ENABLE_WRITEBACK = os.getenv("ENABLE_WRITEBACK", "false").lower() == "true"

def writeback_note(ticket_id: int, content: str, actor="ai"):
    if not ENABLE_WRITEBACK:
        log_event({
            "type": "writeback_blocked",
            "ticket_id": ticket_id,
            "actor": actor
        })
        return {"status": "blocked"}

    add_note_to_ticket(ticket_id, content)

    log_event({
        "type": "writeback_success",
        "ticket_id": ticket_id,
        "actor": actor
    })

    return {"status": "written"}
