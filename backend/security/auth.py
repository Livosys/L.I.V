from fastapi import Request, HTTPException
import os

def require_internal_auth(request: Request):
    token = request.headers.get("x-api-token")
    if token != os.getenv("ADMIN_TOKEN", "ADMIN_TOKEN_123"):
        raise HTTPException(status_code=401, detail="unauthorized")
