import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str):
    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[
            {"role": "system", "content": "Summarize the following IT knowledge base article in simple steps."},
            {"role": "user", "content": text}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
