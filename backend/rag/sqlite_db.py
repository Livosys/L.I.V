import sqlite3, json, os

DB = "/home/shix.livosys.se/backend/rag/vectors.db"

def conn():
    c = sqlite3.connect(DB)
    c.execute("""
    CREATE TABLE IF NOT EXISTS vectors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        emb TEXT
    )
    """)
    return c

def add(text, emb):
    c = conn()
    c.execute("INSERT INTO vectors (text, emb) VALUES (?,?)",
              (text, json.dumps(emb)))
    c.commit()
    c.close()

def search(q_emb, k=5):
    c = conn()
    rows = []
    for t,e in c.execute("SELECT text, emb FROM vectors"):
        emb = json.loads(e)
        s = sum(x*y for x,y in zip(q_emb, emb))
        rows.append({"text": t, "score": s})
    c.close()
    rows.sort(key=lambda r: r["score"], reverse=True)
    return rows[:k]
