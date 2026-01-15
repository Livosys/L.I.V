from fastapi import APIRouter, Depends
from core.auth import require_token

router = APIRouter(prefix="/api/write", tags=["Write"])

@router.post("/propose")
def propose(ticket_id: int, text: str, _=Depends(require_token)):
    return {
        "ticket_id": ticket_id,
        "proposal": text,
        "status": "PROPOSED"
    }
