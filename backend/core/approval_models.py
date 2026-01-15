from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from db import Base

class ApprovalRequest(Base):
    __tablename__ = "approval_requests"

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, index=True)
    requester_email = Column(String, index=True)
    approver_email = Column(String, index=True)
    step = Column(String)  # request | manager | admin | executed
    approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
