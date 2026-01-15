from fastapi import APIRouter
from pydantic import BaseModel
import os
import pickle

from rag.text_retriever import retrieve
from rag.answer_engine import answer_query

router = APIRouter(prefix="/api/kb", tags=["KB AI"])

META_FILE = "/opt/shix/data/vectors/meta.pkl"


class SearchRequest(BaseModel):
    query: str
    top_k: int = 3


class SummarizeRequest(BaseModel):
    query: str


@router.get("/all")
def kb_all():
    if not os.path.exists(META_FILE):
        return {"count": 0, "articles": []}

    with open(META_FILE, "rb") as f:
        meta = pickle.load(f)

    articles = []
    seen = set()

    for item in meta:
        source = item.get("source")
        text = item.get("text", "")

        # ✅ Visa ENDAST externa KB-artiklar
        if not source or not source.startswith("http"):
            continue

        if source not in seen:
            seen.add(source)
            articles.append({
                "title": text.split("\n")[0][:120],
                "url": source
            })

    return {
        "count": len(articles),
        "articles": articles
    }


@router.post("/search")
def kb_search(req: SearchRequest):
    return {
        "query": req.query,
        "results": retrieve(req.query, top_k=req.top_k)
    }


@router.post("/summarize")
def kb_summarize(req: SummarizeRequest):
    return answer_query(query=req.query)
