from rag.answer_engine import answer_query

def auto_resolve_decision(ticket_text: str) -> dict:
    """
    Returns:
    {
      can_resolve: bool,
      resolution: str,
      confidence: float
    }
    """

    q = f"""
Analyze the ticket below.
If a clear and safe resolution exists, propose it.
Only approve auto-resolution if confidence is high.

Ticket:
{ticket_text}
"""

    result = answer_query(q)

    answer = result.get("answer", "")

    # Very simple confidence heuristic (can be replaced later)
    confidence = 0.9 if "steps" in answer.lower() else 0.4

    return {
        "can_resolve": confidence >= 0.8,
        "resolution": answer,
        "confidence": confidence
    }
