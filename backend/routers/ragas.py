from fastapi import APIRouter
from pydantic import BaseModel
from backend.rag.evaluator import evaluate

router = APIRouter(prefix="/api/ragas", tags=["ragas"])

class EvalPayload(BaseModel):
    question: str
    context: list
    answer: str

@router.post("")
def ragas(p: EvalPayload):
    return evaluate(p.question, p.context, p.answer)
