from fastapi import APIRouter, Header, HTTPException
from services.freshservice import add_note

router = APIRouter(prefix="/api")

@router.post("/apply")
def apply(payload: dict, x_user: str = Header("unknown")):
    try:
        ticket_id = payload["ticket_id"]
        text = payload["text"]
        private = payload.get("private", True)

        add_note(ticket_id, text, private)

        return {"status": "APPLIED", "ticket_id": ticket_id, "by": x_user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
