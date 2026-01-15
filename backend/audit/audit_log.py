from datetime import datetime

def log_action(action: str, ticket_id: int, actor: str, payload: dict):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "ticket_id": ticket_id,
        "actor": actor,
        "payload": payload
    }

    with open("/opt/shix/data/audit.log", "a") as f:
        f.write(str(entry) + "\n")
