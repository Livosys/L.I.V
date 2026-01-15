from fastapi import APIRouter, Depends, HTTPException
from core.auth import require_token
from services.freshservice import update_ticket

router = APIRouter(prefix="/api/write", tags=["Write"])

@router.post("/apply")
def apply(ticket_id: int, resolution: str, _=Depends(require_token)):
    try:
        payload = {
            "resolution": resolution,
            "status": 4
        }
        update_ticket(ticket_id, payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "ticket_id": ticket_id,
        "status": "APPLIED"
    }
