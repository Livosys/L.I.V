from fastapi import APIRouter, Request, Depends
import json
from security.rbac import require_admin

router = APIRouter(prefix="/api/admin/dashboard", tags=["admin-dashboard"])

@router.get("/stats")
def dashboard_stats(request: Request, _=Depends(require_admin)):
    try:
        with open("/opt/shix/data/search_misses.log") as f:
            misses = [json.loads(l) for l in f.readlines()]
    except FileNotFoundError:
        misses = []

    top_queries = {}
    for m in misses:
        q = m["query"]
        top_queries[q] = top_queries.get(q, 0) + 1

    return {
        "total_misses": len(misses),
        "top_queries": sorted(
            [{"query": k, "count": v} for k, v in top_queries.items()],
            key=lambda x: x["count"],
            reverse=True
        )[:10]
    }
