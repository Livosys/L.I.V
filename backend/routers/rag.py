from fastapi import APIRouter
from rag.semantic import semantic_search

router = APIRouter()

def search_rag(query: str):
    results = semantic_search(query)

    items = []
    for r in results:
        items.append({
            "label": r["title"],
            "action": {
                "type": "link",
                "href": r["url"]
            }
        })

    return {
        "answer": "Här är vad jag hittade",
        "ui": {
            "type": "list",
            "items": items
        }
    }
