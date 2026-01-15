from rag.llm_client import embed_text


def embed_query(text: str) -> list:
    """
    Standard embedding entrypoint för hela SHIX.
    ALL RAG (Vector, Graph, Agentic, RAGAS) ska använda denna.
    """
    return embed_text(text)
