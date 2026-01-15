import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for a list of texts using OpenAI.
    """
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]
