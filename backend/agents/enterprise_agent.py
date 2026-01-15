from audit.audit_log import log

def answer(message: str, context: dict | None = None) -> dict:
    """
    Enterprise Agent entrypoint.
    Orchestrates intent → KB / Tickets / RAG.
    """

    # Audit input
    log(
        event="agent.invoked",
        payload={
            "message": message
        }
    )

    msg = message.lower().strip()

    # VERY SIMPLE FIRST ROUTING (production-safe placeholder)
    if "vpn" in msg:
        response = {
            "answer": "Här är relevant information om VPN.",
            "intent": "kb_search",
            "topic": "vpn"
        }
    else:
        response = {
            "answer": f"Jag tog emot ditt meddelande: {message}",
            "intent": "unknown"
        }

    # Audit output
    log(
        event="agent.responded",
        payload=response
    )

    return response
