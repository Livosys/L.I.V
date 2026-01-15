from datetime import datetime, timezone

def sla_risk_level(sla: dict):
    if not sla or not sla.get("due_by"):
        return "unknown"

    due = datetime.fromisoformat(sla["due_by"].replace("Z","")).replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    minutes_left = (due - now).total_seconds() / 60

    if minutes_left <= 0:
        return "breached"
    if minutes_left < 30:
        return "critical"
    if minutes_left < 90:
        return "warning"
    return "ok"
