from fastapi import APIRouter, Depends, HTTPException
from core.auth import require_token
from services.freshservice import get_ticket

router = APIRouter(prefix="/api/ai", tags=["AI"])

@router.post("/analyze/{ticket_id}")
def analyze_ticket(ticket_id: int, _=Depends(require_token)):
    try:
        ticket = get_ticket(ticket_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "ticket_id": ticket_id,
        "subject": ticket.get("subject"),
        "analysis": "AI analysis placeholder"
    }
