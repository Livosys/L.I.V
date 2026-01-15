import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")

def embed_text(text: str):
    resp = client.embeddings.create(
        model=MODEL,
        input=text
    )
    return resp.data[0].embedding
