def normalize(text: str) -> str:
    return (text or "").strip().lower()

def is_search_intent(text: str) -> bool:
    keywords = ["sök", "leta", "hitta", "kb", "kunskap"]
    return any(k in text for k in keywords)
