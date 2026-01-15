from fastapi import APIRouter, Depends, HTTPException
from security.jwt_guard import require_user
from writeback import execute_approved

router = APIRouter(prefix="/api/writeback", tags=["writeback"])

@router.post("/execute")
def execute(auth=Depends(require_user)):
    user, role = auth

    if role not in ("admin", "agent"):
        raise HTTPException(status_code=403, detail="Not allowed")

    if not user.approval_enabled and not user.is_admin:
        raise HTTPException(status_code=403, detail="Approval not enabled")

    return execute_approved()
