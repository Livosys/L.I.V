def decide(query: str) -> str:
    if "ticket" in query.lower():
        return "tickets"
    return "ai"
