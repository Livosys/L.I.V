def assess_sla(ticket: dict):
    priority = ticket.get("priority", 3)
    status = ticket.get("status", "open")

    if priority == 1 and status != "resolved":
        return {"sla_risk": "high"}

    if priority == 2:
        return {"sla_risk": "medium"}

    return {"sla_risk": "low"}
