from fastapi import APIRouter, Request
from audit.logger import log_event

router = APIRouter(prefix="/api/policy", tags=["policy"])

@router.post("/acknowledge")
async def acknowledge_policy(request: Request):
    data = await request.json()

    log_event({
        "type": "policy_ack",
        "policy": data.get("policy"),
        "version": data.get("version"),
        "user": request.headers.get("X-User-Id", "unknown"),
    })

    return {"status": "acknowledged"}
