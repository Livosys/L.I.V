import datetime
import json

AUDIT_LOG = "/opt/shix/data/audit.log"

def log(event: str, meta: dict | None = None):
    entry = {
        "ts": datetime.datetime.utcnow().isoformat(),
        "event": event,
        "meta": meta or {}
    }
    with open(AUDIT_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
