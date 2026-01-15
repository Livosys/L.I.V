from datetime import datetime

from rag.vector_db import search
from rag.embeddings import embed_query
from rag.graph_retriever import graph_expand
from rag.llm_client import ask_llm


def answer(query: str) -> dict:
    q_emb = embed_query(query)

    # 1️⃣ Vector retrieval
    scored = search(q_emb, top_k=5)
    chunks = [c for _, c in scored]

    # 2️⃣ Graph expansion
    graph_context = graph_expand(chunks)

    # 3️⃣ Kombinera kontext
    context_texts = []
    for c in chunks:
        if c.get("text"):
            context_texts.append(c["text"])

    for g in graph_context:
        text = g["data"].get("text")
        if text:
            context_texts.append(text)

    if not context_texts:
        return {
            "answer": "No relevant information found.",
            "contexts": [],
            "generated_at": datetime.utcnow().isoformat() + "Z"
        }

    prompt = f"""
You are an IT support expert.

Question:
{query}

Context:
""" + "\n\n".join(f"- {t}" for t in context_texts)

    llm_answer = ask_llm(prompt)

    return {
        "answer": llm_answer,
        "contexts": context_texts,
        "generated_at": datetime.utcnow().isoformat() + "Z"
    }
