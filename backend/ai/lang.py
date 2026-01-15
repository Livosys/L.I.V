def detect_language(text: str) -> str:
    if any(w in text.lower() for w in ["hej", "sök", "ärende"]):
        return "sv"
    return "en"
