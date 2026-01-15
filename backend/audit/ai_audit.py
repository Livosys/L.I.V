import json
from datetime import datetime

AUDIT_FILE = "/opt/shix/backend/audit/ai_calls.log"


def log_ai_call(event: dict):
    event["ts"] = datetime.utcnow().isoformat()
    with open(AUDIT_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")
