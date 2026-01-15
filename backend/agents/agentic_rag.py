from rag.graph_rag_answer_engine import answer


def agentic_answer(query: str) -> dict:
    """
    Agentic GraphRAG:
    - vector search
    - graph expansion
    - consolidated answer
    """
    return answer(query)
