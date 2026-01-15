from fastapi import APIRouter
from db import SessionLocal
from core.approval_models import ApprovalRequest

router = APIRouter(prefix="/api/analytics", tags=["analytics"])

@router.get("/approvals")
def approval_stats():
    db = SessionLocal()
    total = db.query(ApprovalRequest).count()
    approved = db.query(ApprovalRequest).filter(ApprovalRequest.approved==True).count()
    db.close()

    return {
        "total_requests": total,
        "approved": approved,
        "approval_rate": (approved / total) if total else 0
    }
