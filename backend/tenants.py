import sqlite3

DB = "/opt/shix/backend/audit.db"

def create_tenant(name, workspace_id):
    with sqlite3.connect(DB) as con:
        con.execute("""
        INSERT INTO tenants (name, workspace_id)
        VALUES (?, ?)
        """, (name, workspace_id))
