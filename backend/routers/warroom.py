from fastapi import APIRouter
from warroom.engine import get_war_room

router = APIRouter()

@router.get("/api/warroom/{mi_id}")
def get_room(mi_id: str):
    room = get_war_room(mi_id)
    if not room:
        return {"error": "War-room not found"}

    return {
        "mi_id": room.mi_id,
        "category": room.category,
        "status": room.status,
        "participants": room.participants,
        "timeline": room.timeline,
        "decisions": room.decisions,
        "updates": room.updates
    }
