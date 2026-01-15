import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("all-MiniLM-L6-v2")
INDEX_PATH = "rag_store/index.faiss"
META_PATH = "rag_store/meta.pkl"

os.makedirs("rag_store", exist_ok=True)

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
    meta = pickle.load(open(META_PATH, "rb"))
else:
    index = faiss.IndexFlatL2(384)
    meta = []

def add_documents(texts, sources):
    embeddings = MODEL.encode(texts)
    index.add(embeddings)
    meta.extend(sources)
    faiss.write_index(index, INDEX_PATH)
    pickle.dump(meta, open(META_PATH, "wb"))

def search(query, k=5):
    emb = MODEL.encode([query])
    D, I = index.search(emb, k)
    return [meta[i] for i in I[0] if i < len(meta)]
