from rag.vector_store import search
from rag.embeddings import embed_query

def retrieve(query: str, top_k: int = 3):
    """
    High-level retriever:
    text -> embedding -> FAISS search
    """
    embedding = embed_query(query)
    return search(embedding, k=top_k)
