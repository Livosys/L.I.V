from fastapi import APIRouter, HTTPException
from backend.freshservice.client import list_tickets

router = APIRouter(
    prefix="/api/tickets",
    tags=["tickets"]
)

@router.get("")
def list_all_tickets():
    try:
        return list_tickets()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
