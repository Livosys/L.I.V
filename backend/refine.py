from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def refine_text(text: str) -> str:
    system_prompt = """
You clean and normalize ITSM data for use in a RAG knowledge base.
- Remove noise
- Keep technical meaning
- Normalize format
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": system_prompt},
                  {"role": "user", "content": text}],
        temperature=0.2
    )
    return response.choices[0].message.content
