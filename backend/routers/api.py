from fastapi import APIRouter
from mcp.orchestrator import run_mcp_from_message

router = APIRouter()

@router.post("/chat")
def chat(payload: dict):
    message = payload.get("message", "")
    return run_mcp_from_message(message)
