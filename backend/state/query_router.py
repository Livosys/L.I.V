from services.intent_classifier import classify_intent

def route_query(message: str):
    intent = classify_intent(message)

    t = intent.get("intent", "UNKNOWN")

    # LIST
    if t == "LIST_TICKETS":
        return {"type": "LIST", "filter": {}}

    # COUNT
    if t == "COUNT_TICKETS":
        return {"type": "COUNT", "filter": {}}

    # OPEN – kräver giltigt ID
    if t == "OPEN_TICKET":
        ticket_id = intent.get("id")
        if isinstance(ticket_id, int) and ticket_id > 0:
            return {"type": "OPEN", "value": ticket_id}
        # fallback
        return {"type": "FACT", "query": message}

    # KB / FACT
    if t in ("KB_SEARCH", "HELP"):
        return {"type": "FACT", "query": message}

    return {"type": "FACT", "query": message}
