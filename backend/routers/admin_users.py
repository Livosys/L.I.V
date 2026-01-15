from fastapi import APIRouter, Depends
from db import SessionLocal
from core.models import UserFlags
from security.jwt_guard import require_user

router = APIRouter(prefix="/api/admin", tags=["admin"])

@router.get("/users")
def list_users(auth=Depends(require_user)):
    user, role = auth
    if role != "admin":
        return []

    db = SessionLocal()
    users = db.query(UserFlags).all()
    db.close()

    return [
        {
            "email": u.email,
            "tenant": u.tenant,
            "is_admin": u.is_admin,
            "approval_enabled": u.approval_enabled
        }
        for u in users
    ]
