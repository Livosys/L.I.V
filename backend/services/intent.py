def classify_intent(message: str):
    text = message.lower()

    ticket_keywords = [
        "fungerar inte",
        "problem",
        "fel",
        "kan inte",
        "kommer inte åt",
        "vpn",
        "inlogg",
        "server",
        "access"
    ]

    matches = sum(1 for k in ticket_keywords if k in text)

    if matches == 0:
        return ("kb", 0.0)

    confidence = min(0.3 + (matches * 0.15), 0.95)
    return ("ticket", confidence)
