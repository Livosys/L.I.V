from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db import Base

class WritebackAudit(Base):
    __tablename__ = "writeback_audit"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    tenant = Column(String)
    action = Column(String)
    ticket_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
