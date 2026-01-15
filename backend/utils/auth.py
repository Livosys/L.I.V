from fastapi import Header, HTTPException

def require_auth(authorization: str = Header(None)):
    if authorization != "Bearer LIV-DEMO-TOKEN":
        raise HTTPException(status_code=401, detail="Unauthorized")
