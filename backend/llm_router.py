import os
from openai import OpenAI

USE_LOCAL = os.getenv("USE_LOCAL_LLM", "false") == "true"
client = OpenAI()

def generate(messages, stream=False):
    if USE_LOCAL:
        # Placeholder för lokal LLM (t.ex. llama.cpp / Ollama)
        if stream:
            for w in "Local LLM response fallback".split():
                yield w + " "
        else:
            return "Local LLM response fallback"
    else:
        return client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            stream=stream
        )
