from fastapi import APIRouter
import subprocess

router = APIRouter(prefix="/ai/observer", tags=["AI"])

@router.get("/analyze")
def analyze():
    result = subprocess.check_output(
        ["python3", "/opt/agentic-ai/tools/observer_ai.py"],
        text=True
    )
    return {"analysis": result}
