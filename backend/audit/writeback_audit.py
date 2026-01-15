from datetime import datetime
import json
import os

AUDIT_FILE = "/opt/shix/data/audit_writeback.log"
os.makedirs("/opt/shix/data", exist_ok=True)

def audit_writeback(session_id: str, ticket_id: int, note: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "ticket_id": ticket_id,
        "note": note
    }
    with open(AUDIT_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
