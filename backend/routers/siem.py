from fastapi import APIRouter
from db import SessionLocal
from core.audit_models import WritebackAudit

router = APIRouter(prefix="/api/siem", tags=["siem"])

@router.get("/writebacks")
def export_writebacks():
    db = SessionLocal()
    rows = db.query(WritebackAudit).all()
    db.close()

    return [
        {
            "timestamp": r.created_at.isoformat(),
            "email": r.email,
            "tenant": r.tenant,
            "action": r.action,
            "ticket_id": r.ticket_id
        }
        for r in rows
    ]
