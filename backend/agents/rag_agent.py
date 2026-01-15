from rag.semantic import semantic_search

SCORE_THRESHOLD = 0.65

def expand_queries(query: str):
    """
    Agentic expansion – ENKEL men effektiv
    """
    return [
        query,
        f"{query} felsökning",
        f"{query} problem",
    ]

def rag_answer(query: str, ticket_context: dict | None = None):
    queries = expand_queries(query)
    all_hits = []

    for q in queries:
        hits = semantic_search(q, top_k=5)
        all_hits.extend(hits)

    # deduplicera på url
    seen = set()
    unique_hits = []
    for h in all_hits:
        url = h.get("url")
        if url and url not in seen:
            seen.add(url)
            unique_hits.append(h)

    strong_hits = [
        h for h in unique_hits
        if h.get("score", 0) >= SCORE_THRESHOLD
    ]

    if not strong_hits:
        return {
            "type": "rag",
            "confidence": "low",
            "items": []
        }

    items = []
    for h in strong_hits:
        items.append({
            "label": h.get("title", "Kunskapsartikel"),
            "url": h.get("url")
        })

    return {
        "type": "rag",
        "confidence": "high",
        "items": items
    }
