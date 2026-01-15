from datetime import datetime, timedelta

PRIORITY_RULES = {
    "critical": {"hours": 1},
    "high": {"hours": 4},
    "medium": {"hours": 8},
    "low": {"hours": 24},
}

def assess_sla(priority: str, created_at: str):
    hours = PRIORITY_RULES.get(priority, PRIORITY_RULES["medium"])["hours"]
    deadline = datetime.fromisoformat(created_at) + timedelta(hours=hours)
    breached = datetime.utcnow() > deadline
    return {"deadline": deadline.isoformat(), "breached": breached}
