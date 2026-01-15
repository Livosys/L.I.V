from fastapi import Request, HTTPException

def require_admin(request: Request):
    role = request.headers.get("X-Role", "")
    if role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
