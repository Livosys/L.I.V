from vector_db import get_collection
from openai import OpenAI

client = OpenAI()

def ingest_text(text: str):
    col = get_collection()

    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding

    doc_id = col.add(
        documents=[text],
        embeddings=[emb],
        ids=[]
    )

    return doc_id[0]
