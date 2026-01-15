import sys
from pathlib import Path

# --- ENSURE PROJECT ROOT IN PYTHONPATH ---
PROJECT_ROOT = Path("/home/shix.livosys.se/backend")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import json
from datetime import datetime
import os
import time

from openai import OpenAI
from services.audit_logger import log_event

# --- OPENAI CLIENT ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

RAG_QUEUE = Path("/home/shix.livosys.se/backend/rag_queue")
VECTOR_STORE = Path("/home/shix.livosys.se/backend/vector_store")
VECTOR_STORE.mkdir(parents=True, exist_ok=True)

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
EMBED_MODEL = "text-embedding-3-large"

def chunk_text(text: str):
    chunks = []
    start = 0
    length = len(text)

    while start < length:
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - CHUNK_OVERLAP

    return chunks

def embed_text(text: str):
    """
    REAL EMBEDDING VIA OPENAI
    """
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=text,
        timeout=10,
    )
    return response.data[0].embedding

def run():
    files = list(RAG_QUEUE.glob("*.json"))
    if not files:
        print("No RAG items to process")
        return

    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            ticket = json.load(fh)

        text = ticket.get("description_text", "")
        if not text:
            f.unlink()
            continue

        chunks = chunk_text(text)
        stored = 0

        for idx, c in enumerate(chunks):
            try:
                emb = embed_text(c)
                time.sleep(0.2)  # gentle rate limiting
            except Exception as e:
                log_event({
                    "component": "chunk_embed",
                    "ticket_id": ticket.get("id"),
                    "status": "embedding_error",
                    "error": str(e)
                })
                continue

            record = {
                "ticket_id": ticket.get("id"),
                "chunk_index": idx,
                "text": c,
                "embedding": emb,
                "source": ticket.get("source"),
                "created_at": datetime.utcnow().isoformat() + "Z",
                "model": EMBED_MODEL,
            }

            out = VECTOR_STORE / f"t{ticket.get('id')}_c{idx}.json"
            with open(out, "w", encoding="utf-8") as oh:
                json.dump(record, oh, ensure_ascii=False, indent=2)

            stored += 1

        log_event({
            "component": "chunk_embed",
            "ticket_id": ticket.get("id"),
            "chunks": stored,
            "model": EMBED_MODEL,
            "status": "ok"
        })

        f.unlink()
        print(f"Processed ticket {ticket.get('id')} → {stored} chunks")

if __name__ == "__main__":
    run()
