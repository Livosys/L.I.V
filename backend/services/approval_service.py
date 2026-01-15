import json
import uuid
from datetime import datetime
from pathlib import Path

APPROVAL_FILE = Path("/opt/shix/backend/data/approvals.json")
APPROVAL_FILE.parent.mkdir(parents=True, exist_ok=True)

def _load():
    if APPROVAL_FILE.exists():
        return json.loads(APPROVAL_FILE.read_text())
    return []

def _save(data):
    APPROVAL_FILE.write_text(json.dumps(data, indent=2))

def create_approval(ticket_id, decision, reason):
    approvals = _load()
    approval = {
        "id": str(uuid.uuid4()),
        "ticket_id": ticket_id,
        "decision": decision,
        "reason": reason,
        "status": "PENDING",
        "created_at": datetime.utcnow().isoformat()
    }
    approvals.append(approval)
    _save(approvals)
    return approval

def list_pending():
    return [a for a in _load() if a["status"] == "PENDING"]

def list_approved():
    return [a for a in _load() if a["status"] == "APPROVED"]

def decide(approval_id, approved: bool, actor="human"):
    approvals = _load()
    for a in approvals:
        if a["id"] == approval_id:
            a["status"] = "APPROVED" if approved else "REJECTED"
            a["decided_by"] = actor
            a["decided_at"] = datetime.utcnow().isoformat()
            _save(approvals)
            return a
    return None
