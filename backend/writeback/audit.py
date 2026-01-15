from db import SessionLocal
from core.audit_models import WritebackAudit

def log_writeback(email, tenant, ticket_id):
    db = SessionLocal()
    db.add(
        WritebackAudit(
            email=email,
            tenant=tenant,
            action="write_note",
            ticket_id=ticket_id
        )
    )
    db.commit()
    db.close()
