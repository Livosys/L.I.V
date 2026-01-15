from fastapi import Header, HTTPException
from db import SessionLocal
from core.models import UserFlags

def require_approval_enabled(x_user_email: str = Header(...)):
    db = SessionLocal()
    user = db.query(UserFlags).filter(UserFlags.email == x_user_email).first()
    db.close()

    if not user:
        raise HTTPException(status_code=403, detail="User not found")

    if not user.approval_enabled and not user.is_admin:
        raise HTTPException(status_code=403, detail="Approval not enabled")

    return user
