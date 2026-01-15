import os
from openai import OpenAI
from services.search import search

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rag_answer(query: str):
    context = "\n---\n".join(search(query))

    prompt = f"""
You are an ITSM expert assistant.
Use ONLY the context below.

Context:
{context}

Question:
{query}
"""

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2
    )
    return r.choices[0].message.content
