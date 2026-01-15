from audit.audit_log import log_action

_pending = {}

def request_approval(ticket_id: int, change: dict, requested_by: str):
    _pending[ticket_id] = change
    log_action(
        action="WRITEBACK_REQUESTED",
        ticket_id=ticket_id,
        actor=requested_by,
        payload=change
    )
    return True

def approve(ticket_id: int, approver: str):
    change = _pending.pop(ticket_id, None)
    if not change:
        return False

    log_action(
        action="WRITEBACK_APPROVED",
        ticket_id=ticket_id,
        actor=approver,
        payload=change
    )
    return change
