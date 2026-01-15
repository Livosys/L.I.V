from db import engine
from core.models import UserFlags

UserFlags.metadata.create_all(bind=engine)
print("OK: user_flags table ensured")
