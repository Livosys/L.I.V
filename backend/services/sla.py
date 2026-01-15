from datetime import datetime, timezone
import services.freshservice as fs

def sla_risk():
    data = fs.my_tickets()
    tickets = data.get("tickets", [])
    now = datetime.now(timezone.utc)

    at_risk = []
    for t in tickets:
        due = t.get("due_by")
        if due:
            due_dt = datetime.fromisoformat(due.replace("Z","+00:00"))
            if due_dt <= now:
                at_risk.append(t)

    return {
        "total_open": len(tickets),
        "sla_risk": len(at_risk)
    }
