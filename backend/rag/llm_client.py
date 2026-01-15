"""
LLM Client – Enterprise Safe (READ ONLY)
----------------------------------------
Compatible with installed OpenAI SDK.
Provides:
- chat()
- ask()
- ask_llm()
- embed_text()
"""

import os
import logging
import openai

log = logging.getLogger("llm")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set")

openai.api_key = OPENAI_API_KEY

# ---------------------------------------------------------
# CHAT / COMPLETION
# ---------------------------------------------------------

def chat(prompt: str, context: str = "") -> str:
    messages = []

    if context:
        messages.append({
            "role": "system",
            "content": f"Context:\n{context}"
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.2
    )

    return resp["choices"][0]["message"]["content"].strip()


def ask(prompt: str) -> str:
    return chat(prompt)


def ask_llm(prompt: str, context: str = "") -> str:
    return chat(prompt, context)

# ---------------------------------------------------------
# EMBEDDINGS
# ---------------------------------------------------------

def embed_text(text: str) -> list:
    resp = openai.Embedding.create(
        model="text-embedding-3-small",
        input=text
    )
    return resp["data"][0]["embedding"]
