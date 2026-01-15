from collections import Counter
from services.sla_risk import sla_risk_level

def detect_major_incident(tickets: list):
    if len(tickets) < 5:
        return False, None

    categories = Counter(t.get("category") for t in tickets)
    most_common_cat, count = categories.most_common(1)[0]

    critical = [
        t for t in tickets
        if sla_risk_level(t.get("sla")) in ["critical", "breached"]
    ]

    if count >= 3 and len(critical) >= 2:
        return True, {
            "type": "MAJOR_INCIDENT",
            "category": most_common_cat,
            "ticket_count": len(tickets),
            "critical_tickets": len(critical)
        }

    return False, None
