import sqlite3
from datetime import datetime, timedelta

DB_PATH = "/opt/shix/backend/audit.db"

def rank_articles(user_id: str, articles: list):
    """
    articles = list of dicts with keys:
      article_id, title, excerpt, url, citation_id
    """

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    ranked = []

    for a in articles:
        score = 0
        article_id = a["article_id"]

        # 1️⃣ User usage (last 7 days)
        cur.execute("""
            SELECT COUNT(*) FROM kb_usage_log
            WHERE user_id = ?
              AND article_id = ?
              AND timestamp > datetime('now', '-7 days')
        """, (user_id, article_id))
        user_hits = cur.fetchone()[0]
        score += min(user_hits, 5)

        # 2️⃣ Org trend (last 7 days)
        cur.execute("""
            SELECT COUNT(*) FROM kb_usage_log
            WHERE article_id = ?
              AND timestamp > datetime('now', '-7 days')
        """, (article_id,))
        org_hits = cur.fetchone()[0]
        score += min(org_hits // 3, 3)

        # 3️⃣ Freshness (placeholder – kan förbättras senare)
        score += 1  # neutral baseline

        ranked.append({
            **a,
            "score": score
        })

    conn.close()

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked
