def is_ticket_intent(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    keywords = [
        "ticket",
        "ärende",
        "ärenden",
        "mina tickets",
        "mina ärenden",
        "status"
    ]
    return any(k in t for k in keywords)
