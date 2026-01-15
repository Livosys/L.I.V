import os
import json
import subprocess

def ai_intent(text: str):
    if not os.getenv("OPENAI_API_KEY"):
        return None

    p = subprocess.run(
        ["codex", "run"],
        input=text,
        text=True,
        capture_output=True,
        timeout=10
    )

    raw = (p.stdout or "").strip()
    try:
        return json.loads(raw)
    except:
        return None
