from db import SessionLocal
from core.models import UserFlags

db = SessionLocal()

email = "admin@livosys.se"
user = db.query(UserFlags).filter(UserFlags.email == email).first()

if not user:
    user = UserFlags(
        email=email,
        is_admin=True,
        approval_enabled=True
    )
    db.add(user)
    db.commit()
    print("Admin user created")
else:
    print("Admin user already exists")

db.close()
