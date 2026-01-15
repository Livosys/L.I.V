from services.embeddings import embed
from services.vector_db import add_vector

def ingest_text(source: str, text: str):
    e = embed(text)
    add_vector(source, text, e)
