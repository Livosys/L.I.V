def detect_intent(message: str) -> str:
    m = message.lower()

    if any(k in m for k in ["kb", "artikel", "guide", "kunskap"]):
        return "kb"

    if any(k in m for k in ["vpn", "fungerar inte", "problem", "troubleshooting", "fel"]):
        return "troubleshoot"

    if any(k in m for k in ["skapa ärende", "ticket", "anmäl", "incident"]):
        return "ticket"

    return "chat"
