import sqlite3
from datetime import datetime

DB_PATH = "audit.db"

def log_action(user: str, action: str, ticket_id: int, content: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        action TEXT NOT NULL,
        ticket_id INTEGER,
        content TEXT,
        created_at TEXT NOT NULL
    )
    """)

    cur.execute("""
    INSERT INTO audit_log (user, action, ticket_id, content, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (
        user,
        action,
        ticket_id,
        content,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()
