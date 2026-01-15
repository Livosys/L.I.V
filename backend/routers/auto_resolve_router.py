from fastapi import APIRouter
from pydantic import BaseModel
from rag.auto_resolve_engine import auto_resolve_decision
from services.freshservice_writeback import add_resolution, resolve_ticket

router = APIRouter(prefix="/rag", tags=["auto-resolve"])

class AutoResolveRequest(BaseModel):
    ticket_id: int
    ticket_text: str

@router.post("/auto-resolve")
def auto_resolve(req: AutoResolveRequest):
    decision = auto_resolve_decision(req.ticket_text)

    if decision["can_resolve"]:
        add_resolution(req.ticket_id, decision["resolution"])
        resolve_ticket(req.ticket_id)

    return decision
