import os
import requests

DOMAIN = os.getenv("FRESHSERVICE_DOMAIN")
API_KEY = os.getenv("FRESHSERVICE_API_KEY")

BASE_URL = f"https://{DOMAIN}/api/v2"
AUTH = (API_KEY, "X")

def _get(path, params=None):
    r = requests.get(f"{BASE_URL}{path}", auth=AUTH, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def list_articles():
    data = _get("/solutions/articles")
    articles = data.get("articles", [])
    out = []
    for a in articles:
        out.append({
            "id": a.get("id"),
            "title": a.get("title"),
            "url": f"https://{DOMAIN}/a/solutions/articles/{a.get('id')}"
        })
    return out

def search_articles(query: str):
    data = _get("/solutions/articles/search", params={"query": query})
    articles = data.get("articles", [])
    out = []
    for a in articles:
        out.append({
            "id": a.get("id"),
            "title": a.get("title"),
            "url": f"https://{DOMAIN}/a/solutions/articles/{a.get('id')}"
        })
    return out
