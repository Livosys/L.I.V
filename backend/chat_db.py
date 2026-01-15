import sqlite3
from datetime import datetime

DB_PATH = "/home/shix.livosys.se/backend/chat_history.db"

def get_conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        content TEXT,
        session_id TEXT,
        created_at TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_message(role, content, session_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        "INSERT INTO messages (role, content, session_id, created_at) VALUES (?, ?, ?, ?)",
        (role, content, session_id, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

def get_messages(session_id, limit=50):
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        "SELECT role, content FROM messages WHERE session_id=? ORDER BY id DESC LIMIT ?",
        (session_id, limit)
    )
    rows = c.fetchall()
    conn.close()
    return rows[::-1]
