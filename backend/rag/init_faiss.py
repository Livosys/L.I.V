import faiss
import os

INDEX_PATH = "/opt/shix/backend/rag/kb.index"
DIM = 1536  # OpenAI embeddings dimension

if not os.path.exists(INDEX_PATH):
    index = faiss.IndexFlatL2(DIM)
    faiss.write_index(index, INDEX_PATH)
    print("✅ FAISS index created:", INDEX_PATH)
else:
    print("ℹ️ FAISS index already exists")
