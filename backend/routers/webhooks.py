from fastapi import APIRouter

router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])

@router.post("/approval")
def webhook_approval(payload: dict):
    return {
        "received": True,
        "request_id": payload.get("request_id"),
        "approved_by": payload.get("user")
    }
