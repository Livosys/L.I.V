from fastapi import APIRouter

router = APIRouter()

@router.post("/tickets/followup")
async def tickets_followup(payload: dict):
    message = payload.get("message", "").lower()

    if message in ["visa ärenden", "visa alla ärenden", "ärenden"]:
        return {
            "type": "followup",
            "text": "Hur vill du se ärenden?",
            "options": [
                {
                    "label": "Visa relevanta ärenden (AI)",
                    "value": "tickets_relevant"
                },
                {
                    "label": "Filtrera på kategori",
                    "value": "tickets_filter"
                },
                {
                    "label": "Visa som klickbara kort",
                    "value": "tickets_cards"
                },
                {
                    "label": "Visa som lista",
                    "value": "tickets_list"
                }
            ]
        }

    return {"type": "pass"}
