from typing import List
from services.kb_analytics import log_kb_usage

def summarize(text: str, max_len: int = 280) -> str:
    if not text:
        return "Ingen sammanfattning tillgänglig."
    text = text.replace("\n", " ").strip()
    return text[:max_len] + ("…" if len(text) > max_len else "")

def format_kb_answer(articles: List[dict], tenant: str) -> dict:
    if not articles:
        return {
            "answer": "Jag hittade inga publicerade kunskapsartiklar inom detta ämne.",
            "kb": []
        }

    items = []

    for a in articles[:5]:
        kb_id = a.get("id")
        title = a.get("title", "Okänd titel")

        log_kb_usage(
            tenant=tenant,
            kb_id=kb_id,
            title=title,
            action="view"
        )

        items.append({
            "id": kb_id,
            "title": title,
            "summary": summarize(a.get("description") or a.get("body", "")),
            "url": a.get("portal_url") or a.get("url")
        })

    return {
        "answer": "Här är relevanta kunskapsartiklar:",
        "kb": items
    }
