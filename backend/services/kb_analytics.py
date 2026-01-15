import sqlite3
from datetime import datetime

DB = "/opt/shix/backend/audit.db"

def init_kb_analytics():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS kb_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant TEXT,
            kb_id INTEGER,
            title TEXT,
            action TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_kb_usage(tenant: str, kb_id: int, title: str, action: str):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO kb_usage (tenant, kb_id, title, action, created_at) VALUES (?, ?, ?, ?, ?)",
        (tenant, kb_id, title, action, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()
