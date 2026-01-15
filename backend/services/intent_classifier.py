from openai import OpenAI
import os
import json
import re

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an intent classification engine for an ITSM system.

Rules:
- Output JSON only
- No explanations
- No markdown
- No text outside JSON
- If unclear, intent = "UNKNOWN"

Allowed intents:
LIST_TICKETS
COUNT_TICKETS
OPEN_TICKET
KB_SEARCH
HELP
UNKNOWN

If intent is OPEN_TICKET, include field: id (number)
"""

def classify_intent(message: str) -> dict:
    resp = client.responses.create(
        model="gpt-5.1-codex-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    )

    text = resp.output_text.strip()

    # säker JSON-extraktion (Copilot-style)
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return {"intent": "UNKNOWN"}

    try:
        return json.loads(match.group(0))
    except Exception:
        return {"intent": "UNKNOWN"}
