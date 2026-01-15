from fastapi import APIRouter
from pydantic import BaseModel
from rag.answer_engine import answer_query

router = APIRouter(prefix="/rag", tags=["rag"])

class Query(BaseModel):
    query: str

@router.post("/ask")
def ask(q: Query):
    return answer_query(q.query)
