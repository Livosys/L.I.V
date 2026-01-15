def classify_intent(message: str) -> str:
    if not message:
        return "HELP"
    msg = message.lower()
    if "vpn" in msg or "kb" in msg:
        return "KB_SEARCH"
    return "HELP"
