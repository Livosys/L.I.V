from fastapi import APIRouter, Depends
from security.tenant_guard import require_admin
from rag.vector_store import reload_index

router = APIRouter(prefix="/api/admin", tags=["Admin"])

@router.post("/reload-index")
def reload_vector_index(user=Depends(require_admin)):
    reload_index()
    return {"status": "ok", "message": "Vector index reloaded"}
