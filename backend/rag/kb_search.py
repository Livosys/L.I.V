from freshservice.kb_client import get_categories, get_folders, get_articles

def rag_search(query: str, limit=10):
    hits = []
    for c in get_categories():
        for f in get_folders(c["id"]):
            for a in get_articles(f["id"]):
                if query.lower() in a["title"].lower():
                    hits.append({
                        "id": a["id"],
                        "title": a["title"],
                        "url": a["url"],
                        "breadcrumb": [c["name"], f["name"]]
                    })
                if len(hits) >= limit:
                    return hits
    return hits
