from fastapi import APIRouter

router = APIRouter()


@router.get("/api/help")
def help_api():
    return {
        "title": "L.I.V – Hjälp",
        "description": "Så här kan du använda chatten.",
        "quick_actions": [
            {"label": "Visa mina ärenden", "command": "visa mina ärenden"},
            {"label": "Lista changes", "command": "lista changes"},
            {"label": "Simulera change", "command": "simulera change 123"},
        ],
        "examples": [
            "visa mina ärenden",
            "4",
            "lista changes",
            "simulera change 123"
        ],
        "limitations": [
            "Read-only mot Freshservice",
            "Skapar eller ändrar inget"
        ]
    }
