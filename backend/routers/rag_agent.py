from fastapi import APIRouter, Request

from agents.rag_agent import rag_answer

router = APIRouter(
    prefix="/api/rag",
    tags=["rag"]
)

@router.post("")
async def rag_endpoint(request: Request):
    body = await request.json()
    query = body.get("query", "")
    return rag_answer(query)
