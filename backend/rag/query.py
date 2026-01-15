import json
from typing import Optional

KB_PATH = "/opt/shix/backend/rag/store.json"

def load_kb():
    try:
        with open(KB_PATH) as f:
            return json.load(f)
    except Exception:
        return []

def list_kb_articles():
    kb = load_kb()
    return [{"id": a.get("id"), "title": a.get("title")} for a in kb]

def get_article_by_id(article_id: int) -> Optional[dict]:
    kb = load_kb()
    for a in kb:
        if a.get("id") == article_id:
            return a
    return None

def keyword_search(question: str) -> Optional[str]:
    kb = load_kb()
    q = question.lower()
    for a in kb:
        if q in a.get("content", "").lower():
            return a.get("content")
    return None
