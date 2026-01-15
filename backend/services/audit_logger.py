import json
from datetime import datetime
from pathlib import Path

AUDIT_DIR = Path("/home/shix.livosys.se/backend/audit")
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

AUDIT_FILE = AUDIT_DIR / "controlled_fetch.log"

def log_event(event: dict):
    record = {
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        **event
    }

    with open(AUDIT_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
