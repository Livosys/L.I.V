import json
import math
from pathlib import Path

DB_PATH = Path("rag/vector_db.json")

def _load():
    if DB_PATH.exists():
        return json.loads(DB_PATH.read_text())
    return []

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    return dot / (na * nb + 1e-9)

def search(query_embedding, top_k=5):
    data = _load()
    scored = []

    for d in data:
        emb = d.get("embedding")
        if not emb:
            continue
        score = cosine(query_embedding, emb)
        scored.append((score, d))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:top_k]]
