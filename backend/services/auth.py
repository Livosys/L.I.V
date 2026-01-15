from fastapi import Header, HTTPException

def require_auth(x_role: str = Header("viewer")):
    return x_role
