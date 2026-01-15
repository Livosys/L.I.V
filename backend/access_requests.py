import sqlite3
from datetime import datetime

DB = "/opt/shix/backend/audit.db"

def request_access(ticket_id, user):
    with sqlite3.connect(DB) as con:
        con.execute("""
        INSERT INTO access_requests (ticket_id, user, status, created_at)
        VALUES (?, ?, 'pending', ?)
        """, (ticket_id, user, datetime.utcnow()))
