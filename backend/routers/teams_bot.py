from fastapi import APIRouter
from pydantic import BaseModel
from routers.rag import rag

router = APIRouter(tags=["Teams"])

class TeamsMessage(BaseModel):
    text: str

@router.post("/teams/message")
def teams_message(msg: TeamsMessage):
    return rag({"query": msg.text})
