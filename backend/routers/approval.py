from fastapi import APIRouter, Depends, HTTPException
from db import SessionLocal
from core.approval_models import ApprovalRequest
from security.jwt_guard import require_user

router = APIRouter(prefix="/api/approval", tags=["approval"])

@router.post("/request/{ticket_id}")
def request_approval(ticket_id: int, auth=Depends(require_user)):
    user, role = auth
    db = SessionLocal()
    req = ApprovalRequest(
        ticket_id=ticket_id,
        requester_email=user.email,
        approver_email="manager@livosys.se",
        step="request"
    )
    db.add(req)
    db.commit()
    db.close()
    return {"status":"requested","ticket_id":ticket_id}

@router.post("/approve/{request_id}")
def approve(request_id: int, auth=Depends(require_user)):
    user, role = auth
    if role not in ("manager","admin"):
        raise HTTPException(status_code=403, detail="Not allowed")

    db = SessionLocal()
    req = db.query(ApprovalRequest).get(request_id)
    req.approved = True
    req.step = "admin" if role=="manager" else "executed"
    db.commit()
    db.close()
    return {"status":"approved","step":req.step}
