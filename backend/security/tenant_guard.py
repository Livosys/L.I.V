import os
from fastapi import Header, HTTPException

TENANT_API_KEY = os.getenv("TENANT_API_KEY")
TENANT_ID = os.getenv("TENANT_ID", "unknown")

def validate_tenant(x_tenant_key: str):
    if x_tenant_key != TENANT_API_KEY:
        raise HTTPException(status_code=403, detail="Invalid tenant key")
    return True

def get_tenant_id(x_tenant_key: str):
    validate_tenant(x_tenant_key)
    return TENANT_ID

# 🔐 TEMP ADMIN GUARD (kan bytas mot RBAC senare)
def require_admin(x_tenant_key: str = Header(None)):
    validate_tenant(x_tenant_key)
    return {"tenant": TENANT_ID, "role": "admin"}
