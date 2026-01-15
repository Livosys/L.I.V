from approval.store import create_approval
from audit.logger import log_event

def propose_writeback(ticket_id: int, content: str):
    approval = create_approval(ticket_id, content)

    log_event({
        "type": "writeback_proposed",
        "ticket_id": ticket_id,
        "approval_id": approval["id"]
    })

    return {
        "status": "pending_approval",
        "approval_id": approval["id"]
    }
