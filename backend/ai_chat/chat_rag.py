from fastapi import APIRouter
from rag.pipeline import retrieve_answer_context
from ai_chat.ai_prompt import SYSTEM_PROMPT
from openai import OpenAI
import os

router = APIRouter()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@router.post("/ai/chat")
async def chat_rag(payload: dict):
    user_msg = payload.get("message", "")

    # Fetch relevant RAG chunks
    chunks = retrieve_answer_context(user_msg, top_k=5)

    context_text = "\n\n".join([c["text"] for c in chunks])

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "system", "content": f"RAG DATA:\\n{context_text}"},
        {"role": "user", "content": user_msg}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    return {"reply": response.choices[0].message.content}
