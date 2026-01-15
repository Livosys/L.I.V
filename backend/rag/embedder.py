from openai import OpenAI

client = OpenAI()

def embed(text: str):
    try:
        r = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return r.data[0].embedding
    except Exception:
        return [0.0] * 1536
