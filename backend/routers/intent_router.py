from fastapi import APIRouter
from intent.engine import detect_intent
from mcp.orchestrator import run_mcp

router = APIRouter()

@router.post("/api/chat")
def chat(payload: dict):
    text = payload.get("message", "")
    intent_data = detect_intent(text)

    intent = intent_data.get("intent")
    params = intent_data.get("params", {})

    return run_mcp(intent, params)
