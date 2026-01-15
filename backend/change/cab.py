from audit.audit_log import log_action

_CAB = {}

def submit_to_cab(change_id: str, impact: dict, requester: str):
    _CAB[change_id] = {
        "change_id": change_id,
        "impact": impact,
        "status": "pending",
        "requester": requester,
        "approver": None
    }
    log_action("CAB_SUBMITTED", 0, requester, {"change_id": change_id})

def approve(change_id: str, approver: str):
    _CAB[change_id]["status"] = "approved"
    _CAB[change_id]["approver"] = approver
    log_action("CAB_APPROVED", 0, approver, {"change_id": change_id})

def reject(change_id: str, approver: str, reason: str):
    _CAB[change_id]["status"] = "rejected"
    _CAB[change_id]["approver"] = approver
    _CAB[change_id]["reason"] = reason
    log_action("CAB_REJECTED", 0, approver, {"change_id": change_id, "reason": reason})

def list_pending():
    return [v for v in _CAB.values() if v["status"] == "pending"]
from notify.customer import build_message, notify

def approve(change_id: str, approver: str):
    change = _CAB[change_id]
    change["status"] = "approved"
    change["approver"] = approver

    if change["impact"]["impact"]["sla_risk"] != "low":
        message = build_message(
            change["impact"]["change"],
            change["impact"]["impact"]
        )
        notify(change["impact"]["users"], message)

    log_action("CAB_APPROVED", 0, approver, {"change_id": change_id})
from notify.customer import build_message, notify

def approve(change_id, approver):
    change = _CAB[change_id]
    change["status"] = "approved"
    change["approver"] = approver

    if change["impact"]["impact"]["sla_risk"] != "low":
        msg = build_message(
            change["impact"]["change"],
            change["impact"]["impact"]
        )
        notify(change["impact"]["users"], msg)
