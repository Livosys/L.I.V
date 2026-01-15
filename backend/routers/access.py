from fastapi import APIRouter, Depends
from security.jwt_guard import require_role
from access_requests import request_access

router = APIRouter(prefix="/api/access")

@router.post("/request")
def access_request(payload: dict, user=Depends(require_role("agent"))):
    request_access(payload["ticket_id"], user["sub"])
    return {"status": "requested"}
