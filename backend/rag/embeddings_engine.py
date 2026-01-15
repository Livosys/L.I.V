import os
import numpy as np
from ai.openai_client import get_client

client = get_client()

PROVIDER = os.getenv("OPENAI_PROVIDER", "openai")

MODEL = (
    os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    if PROVIDER == "azure"
    else os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
)

def embed(text: str):
    res = client.embeddings.create(
        model=MODEL,
        input=text
    )
    return np.array(res.data[0].embedding, dtype="float32")
