from services.search import search

def auto_propose(ticket_text: str):
    ctx = search(ticket_text, top_k=1)
    if not ctx:
        return None
    return f"AI proposal based on history: {ctx[0]}"
