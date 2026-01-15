from fastapi import Request, HTTPException

API_KEYS = {
    "shix-secret-key": "admin",
    "tenant-acme-key": "acme",
    "tenant-beta-key": "beta"
}

async def api_key_guard(request: Request):
    key = request.headers.get("X-API-Key")
    if key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Unauthorized")
    request.state.tenant = API_KEYS[key]
