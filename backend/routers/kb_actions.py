from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/kb", tags=["kb-actions"])

class KBActionPayload(BaseModel):
    kb_id: int
    action: str

@router.post("/action")
def kb_action(payload: KBActionPayload):
    if payload.action == "open":
        return {"result": "open", "kb_id": payload.kb_id}

    if payload.action == "summarize":
        return {
            "result": "summary",
            "kb_id": payload.kb_id,
            "summary": "Automatisk sammanfattning genererad av L.I.V"
        }

    return {"error": "Okänd action"}
