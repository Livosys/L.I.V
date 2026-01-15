from fastapi import Request, HTTPException

ALLOWED = ["127.0.0.1"]

def ip_guard(request: Request):
    if request.client.host not in ALLOWED:
        raise HTTPException(status_code=403, detail="IP blocked")
