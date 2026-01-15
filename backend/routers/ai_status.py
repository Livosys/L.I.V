from fastapi import APIRouter
import subprocess

router = APIRouter(prefix="/ai/status", tags=["AI"])

@router.get("")
def status():
    out = subprocess.check_output(
        ["python3", "/opt/agentic-ai/tools/observer_ai.py"],
        text=True
    )
    return {"text": out}
