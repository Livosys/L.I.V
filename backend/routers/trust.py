from fastapi import APIRouter, Request
from pathlib import Path
import json

router = APIRouter(prefix="/api/trust", tags=["trust"])

AUDIT_LOG = Path("/opt/shix/data/audit.log")

@router.get("/overview")
def trust_overview(request: Request):
    user = request.headers.get("X-User-Id", "unknown")

    acknowledged = {}

    if AUDIT_LOG.exists():
        with AUDIT_LOG.open() as f:
            for line in f:
                try:
                    event = json.loads(line)
                except Exception:
                    continue

                if (
                    event.get("type") == "policy_ack"
                    and event.get("user") == user
                ):
                    acknowledged[event.get("policy")] = event.get("version")

    return {
        "user": user,
        "acknowledged_policies": acknowledged,
    }
