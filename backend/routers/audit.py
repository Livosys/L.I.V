from fastapi import APIRouter, Query
from pathlib import Path
import json

router = APIRouter(prefix="/api/audit", tags=["audit"])

AUDIT_LOG = Path("/opt/shix/data/audit.log")

@router.get("/recent")
def recent_events(limit: int = Query(50, le=500)):
    if not AUDIT_LOG.exists():
        return {"events": []}

    with AUDIT_LOG.open() as f:
        lines = f.readlines()[-limit:]

    events = []
    for line in lines:
        try:
            events.append(json.loads(line))
        except Exception:
            continue

    return {
        "count": len(events),
        "events": events
    }
