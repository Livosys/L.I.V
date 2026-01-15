import sqlite3, os, json
import numpy as np

DB_PATH = os.getenv("RAG_DB_PATH", "rag.db")

def connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    with connect() as c:
        c.execute("""
        CREATE TABLE IF NOT EXISTS vectors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            content TEXT,
            embedding TEXT
        )
        """)
        c.commit()

def add_vector(source: str, content: str, embedding: list[float]):
    with connect() as c:
        c.execute(
            "INSERT INTO vectors (source, content, embedding) VALUES (?,?,?)",
            (source, content, json.dumps(embedding))
        )
        c.commit()

def all_vectors():
    with connect() as c:
        rows = c.execute("SELECT content, embedding FROM vectors").fetchall()
        return [(r[0], np.array(json.loads(r[1]))) for r in rows]
