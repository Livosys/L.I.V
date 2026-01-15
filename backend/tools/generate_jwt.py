import jwt
from datetime import datetime, timedelta

SECRET = "SHIX_SECRET"
payload = {
    "sub": "test-user",
    "role": "supervisor",
    "exp": datetime.utcnow() + timedelta(hours=1)
}

print(jwt.encode(payload, SECRET, algorithm="HS256"))
