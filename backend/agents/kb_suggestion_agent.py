from rag.semantic import semantic_search

def suggest_kb(ticket: dict):
    query = f"{ticket.get('subject','')} {ticket.get('description','')}"
    hits = semantic_search(query, top_k=3)

    return [
        {
            "label": h.get("title"),
            "url": h.get("url")
        }
        for h in hits
    ]
