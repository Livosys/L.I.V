TENANTS = {
    "schema": {
        "domain": "schema",
        "api_key": "DIN_FRESHSERVICE_API_KEY_HÄR"
    }
}

def get_tenant(tenant_id: str):
    tenant = TENANTS.get(tenant_id)
    if not tenant:
        raise Exception("Unknown tenant")
    return tenant
