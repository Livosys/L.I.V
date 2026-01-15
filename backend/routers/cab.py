from fastapi import APIRouter
from change.cab import list_pending, approve, reject

router = APIRouter()

@router.get("/api/cab/pending")
def pending():
    return list_pending()

@router.post("/api/cab/approve")
def cab_approve(change_id: str, approver: str):
    approve(change_id, approver)
    return {"status": "approved"}

@router.post("/api/cab/reject")
def cab_reject(change_id: str, approver: str, reason: str):
    reject(change_id, approver, reason)
    return {"status": "rejected"}
