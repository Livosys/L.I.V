def rag_fallback(query: str) -> dict:
    return {
        "answer": f"Jag hittade ingen exakt artikel. Här är generell vägledning för: {query}",
        "confidence": 0.62,
        "source": "rag-fallback"
    }
