from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/debug")
def debug():
    return {
        "OPENAI_API_KEY": bool(os.getenv("OPENAI_API_KEY")),
        "FRESHSERVICE_API_KEY": bool(os.getenv("FRESHSERVICE_API_KEY")),
        "FRESHSERVICE_DOMAIN": os.getenv("FRESHSERVICE_DOMAIN"),
        "FRESHSERVICE_WORKSPACE_ID": os.getenv("FRESHSERVICE_WORKSPACE_ID"),
    }
