from fastapi import APIRouter, Request
from rag.answer_engine import answer_query
from services.freshservice_client import reply, resolve

router = APIRouter(prefix="/api/fresh/auto", tags=["fresh"])

@router.post("/")
def auto(ticket_id: int, q: str, request: Request):
    if request.state.role != "admin":
        return {"error": "forbidden"}

    res = answer_query(q)
    answer = res.get("answer", "")

    reply_res = reply(ticket_id, answer)
    resolve_res = resolve(ticket_id)

    return {
        "reply": reply_res,
        "resolve": resolve_res
    }
