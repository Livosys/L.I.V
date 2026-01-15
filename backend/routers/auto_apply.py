from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.freshservice_writeback import add_note
from security.jwt_guard import require_role

router = APIRouter(tags=["AutoApply"])

class Payload(BaseModel):
    ticket_id: int
    ai_answer: str

@router.post("/tickets/auto-apply")
def auto_apply(
    p: Payload,
    user=Depends(require_role("agent"))
):
    text = f"🤖 SHIX Auto-Svar:\n\n{p.ai_answer}"
    return add_note(p.ticket_id, text, private=True)
