from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_note(ticket_summary: str):
    resp = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),
        messages=[
            {"role":"system","content":"You generate professional ITSM internal notes."},
            {"role":"user","content":ticket_summary}
        ]
    )
    return resp.choices[0].message.content
