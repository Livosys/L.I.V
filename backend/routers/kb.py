from fastapi import APIRouter
from freshservice.kb_client import list_articles, get_article

router = APIRouter()

def list_kb():
    articles = list_articles()
    items = []

    for a in articles:
        items.append({
            "label": a["title"],
            "action": {
                "type": "chat",
                "value": f"kb {a['id']}"
            }
        })

    return {
        "answer": "Här är kunskapsbasen",
        "ui": {
            "type": "list",
            "items": items
        }
    }

def open_kb(ref: str):
    article_id = ref.replace("kb", "").strip()
    a = get_article(article_id)

    return {
        "answer": a["title"],
        "ui": {
            "type": "text",
            "value": a.get("description", "")
        }
    }
