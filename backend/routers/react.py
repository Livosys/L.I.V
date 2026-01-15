from fastapi import APIRouter, Depends
from security.jwt_guard import require_role
from routers.contracts import ReactPayload
from rag.rag_answer_engine import answer_query
from audit.audit_log import audit

router = APIRouter(prefix="/api", tags=["react"])

@router.post("/react")
def react(
    payload: ReactPayload,
    user=Depends(require_role("agent"))
):
    audit("react_call", user, payload.ticket_id)

    answer = answer_query(
        query=payload.goal or "Sammanfatta ärendet",
        ticket_id=payload.ticket_id
    )

    return {
        "ticket_id": payload.ticket_id,
        "goal": payload.goal,
        "answer": answer
    }

@router.get("/react/healthz")
def react_health():
    return {"router": "react", "status": "ok"}
