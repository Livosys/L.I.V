from fastapi import Header, HTTPException

def get_tenant(x_tenant_id: str = Header(None)):
    if not x_tenant_id:
        raise HTTPException(status_code=400, detail="Missing X-Tenant-ID header")
    return x_tenant_id
