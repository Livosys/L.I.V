import sqlite3
from datetime import datetime

DB_PATH = "/opt/shix/backend/audit.db"

def log_kb_usage(user_id: str, article_id: int, action: str):
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS kb_usage_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                article_id INTEGER,
                action TEXT,
                timestamp TEXT
            )
        """)

        cur.execute("""
            INSERT INTO kb_usage_log (user_id, article_id, action, timestamp)
            VALUES (?, ?, ?, ?)
        """, (
            user_id,
            article_id,
            action,
            datetime.utcnow().isoformat()
        ))

        conn.commit()
        conn.close()

    except Exception:
        # Viktigt: loggning får ALDRIG krascha appen
        pass
