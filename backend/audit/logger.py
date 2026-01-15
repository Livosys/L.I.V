from datetime import datetime
import json

LOG_FILE = "/opt/shix/data/audit.log"

def log_event(user, message, intent, params):
    entry = {
        "ts": datetime.utcnow().isoformat(),
        "user": user,
        "message": message,
        "intent": intent,
        "params": params
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
