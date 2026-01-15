import uuid
from refine import refine_text
from chunker import chunk_text
from embedder import get_embedding
from vector_db import add_document
from search import search_knowledgebase

def ingest_document(raw_text: str, source_type="ticket", metadata={}):
    refined = refine_text(raw_text)
    chunks = chunk_text(refined)

    for chunk in chunks:
        emb = get_embedding(chunk)
        doc_id = str(uuid.uuid4())

        full_metadata = {"source": source_type}
        full_metadata.update(metadata)

        add_document(doc_id, chunk, emb, full_metadata)

    return True

def retrieve_answer_context(query: str, top_k=5):
    return search_knowledgebase(query, top_k=top_k)
