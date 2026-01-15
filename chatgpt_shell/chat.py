import os
import json
import subprocess
from openai import OpenAI

BASE_DIR = "/opt/shix/chatgpt_shell"
MEMORY_FILE = f"{BASE_DIR}/memory.json"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are ChatGPT connected to a Linux VPS.

Purpose:
Help the user understand, reason about, and troubleshoot their system through dialogue.

Behavior rules (STRICT):
- Speak freely and naturally, like normal ChatGPT.
- Reason out loud and explain clearly.
- Ask relevant follow-up questions when needed.
- Propose next steps, but NEVER act automatically.
- NEVER run commands unless the user explicitly approves with "ja".

Security:
- Read-only unless approved.
- No file changes, no deletions, no service restarts without approval.
- Freshservice is read-only.

Context:
- Backend: FastAPI + Uvicorn
- OS: Ubuntu VPS
- Runtime: systemd + Nginx
- Goal: understand what is happening and why.

Memory policy:
- Persist useful technical context between sessions.
- Avoid storing secrets.
"""

def run_command(cmd):
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True
    )
    return result.stdout + result.stderr

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)

messages = load_memory()

# Ensure system prompt exists ONCE
if not messages or messages[0].get("role") != "system":
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

print("🧠 ChatGPT (fri chat, kopplad till VPS)")
print("Lokalt minne: AKTIVT")
print("Skriv 'exit' för att avsluta\n")

while True:
    user_input = input("Du: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        save_memory(messages)
        break

    # IGNORE empty input (prevents meta-loop)
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )

    reply = response.choices[0].message.content.strip()
    print("\nChatGPT:", reply, "\n")

    messages.append({"role": "assistant", "content": reply})
    save_memory(messages)

    if reply.startswith("KÖR:"):
        cmd = reply.replace("KÖR:", "").strip()
        confirm = input(f"Vill du köra detta kommando? [{cmd}] (ja/nej): ").strip().lower()
        if confirm == "ja":
            output = run_command(cmd)
            print("\n📟 OUTPUT:\n", output)
            messages.append({"role": "assistant", "content": output})
            save_memory(messages)
