from fastapi import APIRouter, Header, HTTPException
from rag.ticket_index import search
from audit.rag_audit import log_rag
from services.embeddings import embed_text

router = APIRouter(prefix="/api/rag", tags=["RAG"])

@router.post("/tickets")
def rag_tickets(payload: dict, x_tenant_key: str = Header(...)):
    query = payload.get("query")
    if not query:
        raise HTTPException(status_code=400, detail="query missing")

    embedding = embed_text(query)
    results = search(x_tenant_key, embedding)
    log_rag(x_tenant_key, query, results)

    return {"query": query, "results": results}
