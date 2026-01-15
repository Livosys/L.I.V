import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (.env + systemd Environment)
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# Initiera OpenAI-klienten
if API_KEY:
    client = OpenAI(api_key=API_KEY)
else:
    client = None
    print("⚠️ WARNING: OPENAI_API_KEY saknas – AI-funktioner avstängda.")

# -------------------------------------------------------
# EN ENDA FUNKTION: PROCESS_CHAT – används av shix_router
# -------------------------------------------------------

async def process_chat(message: str):
    """
    Tar emot ett meddelande från användaren och returnerar svar från OpenAI Assistant.
    Om API-nyckel saknas returneras ett fallback-svar.
    """

    # Om OpenAI inte är aktivt (ingen API-key)
    if client is None:
        return f"AI-funktionen är inaktiverad – ingen OPENAI_API_KEY hittades.\nDu skrev: {message}"

    if not ASSISTANT_ID:
        return "⚠️ ASSISTANT_ID saknas – lägg till den i systemd eller .env."

    try:
        # 1. Skapa en ny thread
        thread = client.beta.threads.create()

        # 2. Lägg till meddelande i tråden
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=message
        )

        # 3. Starta assistenten
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID
        )

        # 4. Vänta på svar
        while True:
            status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if status.status == "completed":
                break
            time.sleep(0.3)

        # 5. Hämta assistentens svar
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        for msg in messages.data:
            if msg.role == "assistant":
                return msg.content[0].text.value

        return "⚠️ Inget svar från assistenten."

    except Exception as e:
        return f"⚠️ Ett fel uppstod i SHIX-CORE: {str(e)}"
