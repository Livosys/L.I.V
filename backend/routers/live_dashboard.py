from fastapi import APIRouter
from state.live import LIVE

router = APIRouter()

@router.get("/api/dashboard/live")
def live_dashboard():
    return LIVE
