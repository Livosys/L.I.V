from db import SessionLocal, engine, Base
from models.user_flags import UserFlags

Base.metadata.create_all(bind=engine)

db = SessionLocal()

db.merge(UserFlags(
    email="admin@livosys.se",
    is_admin=True,
    approval_enabled=True
))

db.merge(UserFlags(
    email="anna@livosys.se",
    is_admin=False,
    approval_enabled=False
))

db.commit()
db.close()

print("OK: user flags initialized")
