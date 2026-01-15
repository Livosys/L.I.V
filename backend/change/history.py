def analyze_change_history(change, past_tickets: list):
    related_incidents = []

    for t in past_tickets:
        if (
            t.get("category") == change.category
            or change.service in t.get("subject","")
        ):
            related_incidents.append(t)

    mi_count = sum(1 for t in related_incidents if t.get("major_incident"))
    sla_breaches = sum(1 for t in related_incidents if t.get("sla_breached"))

    return {
        "related_incidents": len(related_incidents),
        "major_incidents": mi_count,
        "sla_breaches": sla_breaches
    }
