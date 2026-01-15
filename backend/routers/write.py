from fastapi import APIRouter, Request

router = APIRouter(prefix="/api/write", tags=["write"])

@router.post("/propose")
async def propose(payload: dict, request: Request):
    ticket_id = payload.get("ticket_id")
    text = payload.get("text")

    return {
        "status": "PROPOSED",
        "ticket_id": ticket_id,
        "message": "Proposal saved",
        "text": text
    }

@router.post("/apply")
async def apply(payload: dict, request: Request):
    ticket_id = payload.get("ticket_id")
    text = payload.get("text")

    return {
        "status": "APPLIED",
        "ticket_id": ticket_id,
        "message": "Resolution applied",
        "text": text
    }
