from typing import List

def format_kb_cards(articles: List[dict]) -> list:
    cards = []
    for a in articles:
        cards.append({
            "id": a.get("id"),
            "title": a.get("title"),
            "summary": (a.get("description") or a.get("body") or "")[:300],
            "actions": [
                {"type": "open", "label": "Öppna"},
                {"type": "summarize", "label": "Sammanfatta"}
            ],
            "url": a.get("portal_url") or a.get("url")
        })
    return cards
