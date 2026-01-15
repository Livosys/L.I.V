def build_ticket_summary(ctx: dict):
    ticket = ctx["ticket"]
    requester = ctx["requester"]
    sla = ctx["sla"]

    summary = (
        f"{ticket['subject']} för {requester['department']}.\n"
        f"Status: {ticket['status']}, Prioritet: {ticket['priority']}.\n"
    )

    if sla:
        summary += f"SLA deadline: {sla.get('due_by')}."

    next_action = "Analysera grundorsak och föreslå KB eller eskalering."

    return {
        "summary": summary,
        "next_action": next_action,
        "confidence": 0.78
    }
