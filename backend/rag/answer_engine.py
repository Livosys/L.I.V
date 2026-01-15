from rag.embeddings_engine import embed
from rag.vector_store import search
from ai.openai_client import get_client
import os

client = get_client()

MODEL = (
    os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")
    if os.getenv("OPENAI_PROVIDER") == "azure"
    else os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
)

def answer_query(query: str):
    q_emb = embed(query)
    contexts = search(q_emb, k=3)

    context_text = "\n\n".join(
        f"[{c['source']}]\n{c['text']}" for c in contexts
    ) or "No internal context found."

    messages = [
        {"role": "system", "content": "You are SHIX, an ITSM assistant. Answer strictly from context."},
        {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion:\n{query}"}
    ]

    res = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return {
        "answer": res.choices[0].message.content,
        "sources": [c["source"] for c in contexts]
    }
