import sqlite3
from fastapi import APIRouter, Depends
from security.jwt_guard import require_role

DB = "/opt/shix/backend/audit.db"

router = APIRouter(prefix="/api/analytics", tags=["analytics"])

@router.get("/kb/top")
def top_kb(
    limit: int = 10,
    user=Depends(require_role("admin"))
):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT title, kb_id, COUNT(*) as views
        FROM kb_usage
        GROUP BY kb_id, title
        ORDER BY views DESC
        LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()

    return [
        {
            "kb_id": r[1],
            "title": r[0],
            "views": r[2]
        }
        for r in rows
    ]
