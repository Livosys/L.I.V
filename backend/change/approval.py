_pending_changes = {}

def request_change_approval(change_id: str, impact: dict, requested_by: str):
    _pending_changes[change_id] = {
        "impact": impact,
        "requested_by": requested_by,
        "status": "pending"
    }

def approve_change(change_id: str, approver: str):
    if change_id not in _pending_changes:
        return False

    _pending_changes[change_id]["status"] = "approved"
    _pending_changes[change_id]["approved_by"] = approver
    return True
