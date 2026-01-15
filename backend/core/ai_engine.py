import re
from typing import Optional
from freshservice.kb_client import get_kb_articles
from rag.query import list_kb_articles, get_article_by_id, keyword_search

def detect_intent(message: str) -> str:
    msg = message.lower()
    if any(w in msg for w in ["hej", "hello", "tjena"]):
        return "greeting"
    if any(w in msg for w in ["hjälp", "kan du", "hur gör"]):
        return "help"
    if any(w in msg for w in ["kb", "kunskap", "kunskapsartiklar", "artiklar"]):
        return "list_kb"
    if re.search(r"(visa|öppna)\s+artikel\s+\d+", msg):
        return "show_kb"
    return "general"

def shix_ai_answer(user_message: str, ticket_context: Optional[dict] = None) -> str:
    intent = detect_intent(user_message)

    if intent == "greeting":
        return "Hej! Jag är Liv – din AI för IT Service Management."

    # 🔗 LIVE FRESHSERVICE KB
    try:
        kb_source = get_kb_articles()
    except Exception:
        kb_source = []

    if intent == "list_kb":
        articles = kb_source or list_kb_articles()
        if not articles:
            return "Det finns inga kunskapsartiklar ännu."
        text = "📚 Tillgängliga kunskapsartiklar:\n"
        for a in articles[:10]:
            text += f"• ({a['id']}) {a['title']}\n"
        return text + "\nSäg: Visa artikel 1"

    if intent == "show_kb":
        match = re.search(r"(\d+)", user_message)
        if not match:
            return "Ange vilket artikelnummer du vill visa."
        aid = int(match.group(1))
        for a in kb_source:
            if a["id"] == aid:
                return f"📖 {a['title']}\n\n{a['content']}"
        article = get_article_by_id(aid)
        if article:
            return f"📖 {article['title']}\n\n{article['content']}"
        return "Hittade ingen artikel med det numret."

    kb_answer = keyword_search(user_message)
    if kb_answer:
        return f"📖 Kunskapsartikel:\n{kb_answer}"

    return "Beskriv gärna ärendet så hjälper jag dig vidare."
