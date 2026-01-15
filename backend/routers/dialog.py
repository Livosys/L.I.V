from fastapi import APIRouter
from pydantic import BaseModel
from backend.agents.dialog_agent import dialog_agent

router = APIRouter(prefix="/api/dialog", tags=["dialog"])

class DialogPayload(BaseModel):
    ticket_id: int
    message: str

@router.post("")
def dialog(payload: DialogPayload):
    return dialog_agent(payload.ticket_id, payload.message)
