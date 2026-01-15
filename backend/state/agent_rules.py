def classify_message(message: str) -> str:
    msg = message.strip().lower()

    # HÄLSNING
    if msg in {"hej", "hello", "hi", "hallå"}:
        return "GREETING"

    # TICKET ID
    if msg.isdigit():
        return "TICKET_ID"

    # LISTA TICKETS
    if any(k in msg for k in ["visa", "lista", "ärenden", "tickets", "mina ärenden"]):
        return "LIST_TICKETS"

    # ALLT SOM ÄR EN FRÅGA → RAG
    if len(msg) > 2:
        return "RAG"

    return "UNKNOWN"
