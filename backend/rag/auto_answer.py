from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query, chunk, category, source):
    prompt = f"""
You are SHIX AI Enterprise Assistant.

User question:
{query}

Best knowledge chunk:
{chunk}

Category: {category}
Source file: {source}

Give a clean, professional answer.
"""

    resp = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role":"user","content":prompt}]
    )

    return resp.choices[0].message.content
