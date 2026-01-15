from fastapi import APIRouter, Request, Depends
import json
from security.rbac import require_admin

router = APIRouter(prefix="/api/admin", tags=["admin"])

LOG_FILE = "/opt/shix/data/search_misses.log"

@router.get("/search-misses")
def get_search_misses(request: Request, limit: int = 50, _=Depends(require_admin)):
    try:
        with open(LOG_FILE) as f:
            lines = f.readlines()[-limit:]
            return [json.loads(l) for l in lines]
    except FileNotFoundError:
        return []
