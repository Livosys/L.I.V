from rag.neo4j_client import get_ticket_context

def answer_query(query, ticket_id=None):
    """
    GraphRAG V1 (READ-ONLY)
    - Läser graf-kontext om ticket_id finns
    - Påverkar inte writes eller agents
    """

    graph_context = []
    if ticket_id:
        graph_context = get_ticket_context(ticket_id)

    context_text = ""
    if graph_context:
        context_text = "Graph context:\n"
        for row in graph_context:
            context_text += (
                f"- CI: {row.get('ci_name')} "
                f"({row.get('ci_type')}), "
                f"SLA: {row.get('sla')}, "
                f"Customer: {row.get('customer')}\n"
            )

    # ⚠️ Placeholder – befintlig vector/LLM-RAG ligger efter detta
    answer = f"{context_text}\nAnswer to query: {query}"
    return answer
