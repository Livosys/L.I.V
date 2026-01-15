import os
from typing import List

# Reuse existing components
from vector_db import search_similar_chunks

ENABLE_RAG = os.getenv("ENABLE_RAG", "false") == "true"

class RAGAdapter:
    def __init__(self):
        self.enabled = ENABLE_RAG

    def retrieve(self, query: str, top_k: int = 5) -> List[str]:
        if not self.enabled:
            return []

        try:
            results = search_similar_chunks(query, top_k=top_k)
            return [r["content"] for r in results]
        except Exception as e:
            # Fail safe: never break chat
            return []
