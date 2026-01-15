import sqlite3

conn = sqlite3.connect("shix.db")
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE user_flags ADD COLUMN tenant TEXT DEFAULT 'default'")
    print("Tenant column added")
except Exception as e:
    print("Already exists:", e)

conn.commit()
conn.close()
