def classify_question(query: str) -> str:
    q = query.lower()

    if any(x in q for x in ["hur många", "mina ärenden", "tickets", "ärenden har jag"]):
        return "FRESHSERVICE"

    return "RAG"
