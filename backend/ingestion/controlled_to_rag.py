import sys
from pathlib import Path

# --- ENSURE PROJECT ROOT IN PYTHONPATH ---
PROJECT_ROOT = Path("/home/shix.livosys.se/backend")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import requests
import json
from datetime import datetime

from services.audit_logger import log_event

BACKEND_URL = "http://127.0.0.1:8000/freshservice/tickets/controlled"
RAG_QUEUE_DIR = Path("/home/shix.livosys.se/backend/rag_queue")
RAG_QUEUE_DIR.mkdir(parents=True, exist_ok=True)

def sanitize_ticket(t):
    return {
        "id": t.get("id"),
        "subject": t.get("subject"),
        "status": t.get("status"),
        "priority": t.get("priority"),
        "created_at": t.get("created_at"),
        "updated_at": t.get("updated_at"),
        "description_text": t.get("description_text"),
        "source": "freshservice_controlled",
    }

def run():
    try:
        r = requests.get(BACKEND_URL, timeout=10)
        r.raise_for_status()
        data = r.json()

        tickets = data.get("tickets", [])
        returned = len(tickets)

        log_event({
            "component": "controlled_to_rag",
            "strategy": data.get("strategy"),
            "requested_max": data.get("requested_max"),
            "checked_ids": data.get("checked_ids"),
            "returned": returned,
            "status": "ok"
        })

        if not tickets:
            print("No tickets to ingest")
            return

        for t in tickets:
            safe_ticket = sanitize_ticket(t)
            fname = f"ticket_{safe_ticket['id']}_{int(datetime.utcnow().timestamp())}.json"
            fpath = RAG_QUEUE_DIR / fname

            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(safe_ticket, f, ensure_ascii=False, indent=2)

            print("Queued for RAG:", fpath.name)

    except Exception as e:
        log_event({
            "component": "controlled_to_rag",
            "status": "error",
            "error": str(e)
        })
        raise

if __name__ == "__main__":
    run()
