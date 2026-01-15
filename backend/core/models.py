from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class UserFlags(Base):
    __tablename__ = "user_flags"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    tenant = Column(String, index=True, default="default")

    is_admin = Column(Boolean, default=False)
    approval_enabled = Column(Boolean, default=False)
