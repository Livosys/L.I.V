from fastapi import APIRouter
from pydantic import BaseModel
from rag.pipeline import retrieve_answer_context
from openai import OpenAI
import os

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@router.post("/rag_chat")
def rag_chat(req: ChatRequest):

    # 1. Hämta RAG-chunks
    chunks = retrieve_answer_context(req.message, top_k=5)

    if not isinstance(chunks, list):
        return {"reply": "RAG data format error.", "chunks": []}

    # 2. Omvandla chunks till dokument + metadata
    documents = [c["text"] for c in chunks]
    metadatas = [c["metadata"] for c in chunks]

    context_text = "\n".join(
        [f"[Chunk {i+1}] {documents[i]}" for i in range(len(documents))]
    )

    # 3. Skicka prompt till OpenAI
    prompt = f"""
    You are SHIX AI Overlay. Use the context from Freshservice tickets
    to answer accurately.

    USER QUESTION:
    {req.message}

    CONTEXT FROM RELEVANT CHUNKS:
    {context_text}

    Answer clearly and show understanding of the context.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # 4. KORREKT sätt att läsa svaret i 2025 API
    llm_reply = response.choices[0].message.content

    return {
        "reply": llm_reply,
        "chunks": chunks
    }
