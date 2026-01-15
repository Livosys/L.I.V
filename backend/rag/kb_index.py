from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EMBED_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")

def embed(texts: list[str]):
    return client.embeddings.create(
        model=EMBED_MODEL,
        input=texts
    ).data
