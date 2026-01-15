import os, pickle, numpy as np
import faiss

VECTOR_DIR = "/opt/shix/data/vectors"
INDEX_FILE = f"{VECTOR_DIR}/kb.index"
META_FILE = f"{VECTOR_DIR}/kb.meta"

os.makedirs(VECTOR_DIR, exist_ok=True)

# Minimal embedding (384-dim dummy)
def embed(text):
    return np.array([0.1]*384, dtype="float32")

docs = [{
    "title": "VPN – Installation Guide",
    "category": "VPN",
    "summary": "Step-by-step guide for installing VPN on Windows and macOS.",
    "url": "https://livosys.freshservice.com/a/solutions/articles/58000003580",
    "actions": {"open_kb": "https://livosys.freshservice.com/a/solutions/articles/58000003580"}
}]

embeddings = np.vstack([embed(d["title"] + " " + d["summary"]) for d in docs])

index = faiss.IndexFlatL2(384)
index.add(embeddings)

faiss.write_index(index, INDEX_FILE)
pickle.dump(docs, open(META_FILE, "wb"))

print("KB index built")
