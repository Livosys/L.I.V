from fastapi import APIRouter

router = APIRouter(prefix="/app", tags=["Marketplace"])

@router.get("/sidebar")
def sidebar():
    return {
        "title": "SHIX Assistant",
        "description": "AI-stödd ITSM-assistent",
        "actions": [
            {
                "label": "Sök i ärenden",
                "type": "rag",
                "endpoint": "/api/rag/tickets",
                "placeholder": "Sök i tickets…"
            },
            {
                "label": "Visa mina ärenden",
                "type": "command",
                "command": "visa mina ärenden"
            }
        ]
    }
