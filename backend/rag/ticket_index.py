import os, faiss, pickle
import numpy as np

BASE_DIR = "/opt/shix/data/tickets"

def _paths(tenant):
    tdir = f"{BASE_DIR}/{tenant}"
    os.makedirs(tdir, exist_ok=True)
    return (
        f"{tdir}/index.faiss",
        f"{tdir}/meta.pkl"
    )

def build_index(tenant, embeddings, metadata):
    index_path, meta_path = _paths(tenant)

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, index_path)
    with open(meta_path, "wb") as f:
        pickle.dump(metadata, f)

def search(tenant, query_embedding, top_k=3):
    index_path, meta_path = _paths(tenant)

    if not os.path.exists(index_path):
        return []

    index = faiss.read_index(index_path)
    with open(meta_path, "rb") as f:
        meta = pickle.load(f)

    _, I = index.search(
        np.array([query_embedding]).astype("float32"),
        top_k
    )
    return [meta[i] for i in I[0] if i < len(meta)]
