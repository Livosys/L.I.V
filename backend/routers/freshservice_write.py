from fastapi import APIRouter
from pydantic import BaseModel
from freshservice.client import add_note

router = APIRouter(prefix="/api/freshservice", tags=["Freshservice"])

class NotePayload(BaseModel):
    ticket_id: int
    body: str
    private: bool = True

@router.post("/tickets/note")
def write_note(payload: NotePayload):
    return add_note(
        ticket_id=payload.ticket_id,
        body=payload.body,
        private=payload.private
    )
