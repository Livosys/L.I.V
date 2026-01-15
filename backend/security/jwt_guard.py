from fastapi import Depends, HTTPException, Header
import jwt

SECRET = "SHIX_SECRET_KEY"

def require_role(role: str):
    def guard(authorization: str = Header(...)):
        try:
            token = authorization.replace("Bearer ", "")
            payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            if payload.get("role") != role:
                raise HTTPException(status_code=403, detail="Forbidden")
            return payload
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid token")
    return guard
