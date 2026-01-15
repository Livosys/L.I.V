from backend.infra.redis import get_redis
from datetime import datetime
import json

def request_approval(ticket_id: int, action: dict, requested_by="system"):
    r = get_redis()

    payload = {
        "ticket_id": ticket_id,
        "action": action,
        "requested_by": requested_by,
        "requested_at": datetime.utcnow().isoformat(),
        "status": "pending"
    }

    r.setex(
        f"approval:{ticket_id}",
        3600,
        json.dumps(payload)
    )

    return payload


def approve(ticket_id: int, approved_by: str):
    r = get_redis()
    raw = r.get(f"approval:{ticket_id}")

    if not raw:
        return None

    data = json.loads(raw)
    data["status"] = "approved"
    data["approved_by"] = approved_by
    data["approved_at"] = datetime.utcnow().isoformat()

    r.delete(f"approval:{ticket_id}")
    return data
