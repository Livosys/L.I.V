import sqlite3
from datetime import datetime

DB = "/home/shix.livosys.se/backend/chat_history.db"

def add_usage(session_id: str, tokens: int):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
      CREATE TABLE IF NOT EXISTS usage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        tokens INTEGER,
        created_at TEXT
      )
    """)
    c.execute(
        "INSERT INTO usage (session_id, tokens, created_at) VALUES (?,?,?)",
        (session_id, tokens, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()
