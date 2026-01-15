from fastapi import Header, HTTPException

# I production: lagras i DB eller Vault
API_KEYS = {
    "tenant-acme": "acme-secret-key",
    "tenant-enterprise": "enterprise-secret-key"
}

def require_api_key(
    x_api_key: str = Header(None),
    x_tenant_id: str = Header(None)
):
    if not x_api_key or not x_tenant_id:
        raise HTTPException(status_code=401, detail="Missing API key or tenant")

    valid = API_KEYS.get(x_tenant_id)
    if not valid or valid != x_api_key:
        raise HTTPException(status_code=403, detail="Invalid API key")

    return x_tenant_id
