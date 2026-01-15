from fastapi import APIRouter
from tenants import create_tenant

router = APIRouter(prefix="/api/tenants")

@router.post("/create")
def create(payload: dict):
    create_tenant(payload["name"], payload["workspace_id"])
    return {"status": "tenant_created"}
