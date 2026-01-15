import sqlite3
from routers.react import react

DB = "/opt/shix/backend/audit.db"

def retry_if_approved(ticket_id: int):
    with sqlite3.connect(DB) as con:
        row = con.execute("""
            SELECT status FROM access_requests
            WHERE ticket_id=?
            ORDER BY created_at DESC
            LIMIT 1
        """, (ticket_id,)).fetchone()

    if row and row[0] == "approved":
        # retry supervisor
        react({"ticket_id": ticket_id, "goal": "Auto-retry after approval"})
        return True

    return False
