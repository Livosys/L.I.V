import faiss
import pickle
import numpy as np
from pathlib import Path

BASE_PATH = Path("/opt/shix/data/vectors")
INDEX_FILE = BASE_PATH / "index.faiss"
META_FILE = BASE_PATH / "meta.pkl"

index = faiss.read_index(str(INDEX_FILE))

with open(META_FILE, "rb") as f:
    metadata = pickle.load(f)

def embed(text: str):
    # placeholder – din riktiga embedding används redan i ingest
    return np.zeros((index.d,), dtype="float32")

def query_index(query: str, top_k: int = 5):
    if not isinstance(top_k, int) or top_k <= 0:
        top_k = 5

    qv = embed(query)
    D, I = index.search(np.array([qv]), top_k)

    results = []
    for idx in I[0]:
        if idx < 0:
            continue
        results.append(metadata[idx])

    return results
