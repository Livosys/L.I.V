import jwt, datetime
from fastapi import Header, HTTPException
from backend.security.token_store import is_revoked

PUBLIC_KEY = open("/opt/shix/keys/jwt_public.pem").read()

def require_role(required_role: str):
    def checker(authorization: str = Header(None)):
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing token")

        token = authorization.split(" ", 1)[1]
        try:
            payload = jwt.decode(
                token,
                PUBLIC_KEY,
                algorithms=["RS256"],
                audience="shix",
            )
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")

        if is_revoked(payload.get("jti")):
            raise HTTPException(status_code=401, detail="Token revoked")

        if payload.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")

        return payload
    return checker
