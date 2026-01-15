from freshservice.kb_client import get_kb_articles

def fetch_kb_articles(_query: str):
    articles = get_kb_articles(limit=5)

    results = []
    for a in articles:
        results.append({
            "id": a.get("id"),
            "title": a.get("title"),
            "summary": (a.get("description") or "")[:300]
        })

    return results
