import numpy as np
from services.vector_db import all_vectors
from services.embeddings import embed

def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def search(query: str, top_k=3):
    qv = np.array(embed(query))
    scored = []
    for content, ev in all_vectors():
        scored.append((cosine(qv, ev), content))
    scored.sort(reverse=True)
    return [c for _, c in scored[:top_k]]
