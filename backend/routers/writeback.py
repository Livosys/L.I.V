import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from backend.security.jwt_guard import require_role
from backend.middleware.rate_limit import rate_limit
from backend.freshservice.writeback import add_note
from backend.audit.logger import audit_log

router = APIRouter(
    prefix="/api/writeback",
    tags=["writeback"]
)

class WritebackPayload(BaseModel):
    ticket_id: int
    body: str
    private: bool = True

@router.post("/note")
def write_note(
    payload: WritebackPayload,
    role=Depends(require_role("agent")),
    _=Depends(rate_limit)
):
    if os.getenv("SHIX_WRITEBACK_ENABLED") != "true":
        raise HTTPException(status_code=403, detail="Writeback disabled")

    note_id = add_note(
        payload.ticket_id,
        payload.body,
        payload.private
    )

    audit_log(
        actor="agent",
        action="write_note",
        ticket_id=payload.ticket_id,
        status="success"
    )

    return {
        "status": "ok",
        "ticket_id": payload.ticket_id,
        "freshservice_note_id": note_id,
        "private": payload.private
    }
