import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def ask_llm(prompt: str, context: dict | None = None) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are SHIX, an enterprise ITSM AI assistant. Be concise, factual, and helpful."
        }
    ]

    if context:
        messages.append({
            "role": "system",
            "content": f"Ticket context:\n{context}"
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content
