from fastapi import APIRouter, Depends
from pydantic import BaseModel
from routers.contracts import RagPayload
from security.jwt_guard import require_role
from freshservice.writeback import add_note

router = APIRouter(prefix="/api/tickets", tags=["tickets"])

@router.post("/writeback")
def writeback(
    payload: RagPayload,
    user=Depends(require_role("agent"))
):
    return add_note(
        ticket_id=payload.ticket_id,
        body=payload.body,
        private=payload.private
    )
