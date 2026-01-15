import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer(prompt: str):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a senior IT support engineer. Be concise and actionable."},
            {"role":"user","content":prompt}
        ]
    )
    return r.choices[0].message.content
