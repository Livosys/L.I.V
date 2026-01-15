from datetime import datetime
from dateutil.parser import isoparse

def sla_status(sla_due):
    if not sla_due:
        return "unknown"

    due = isoparse(sla_due)
    now = datetime.utcnow()

    if now > due:
        return "breached"

    remaining = (due - now).total_seconds() / 3600
    if remaining < 1:
        return "at_risk"

    return "ok"
