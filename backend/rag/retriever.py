def retrieve_context(query: str) -> str:
    return "Temporary empty context"

def retrieve(query: str, top_k: int = 3):
    """
    Public retriever wrapper for API usage.
    Returns list of KB chunks with title, content, score.
    """
    try:
        from rag.vector_store import search
        return search(query, top_k=top_k)
    except Exception as e:
        return []
