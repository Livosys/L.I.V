from freshservice.client import get_ticket

# 🔐 Allowed decisions (READ-ONLY)
DECISIONS = {
    "WAIT",
    "RECOMMEND_INTERNAL_NOTE",
    "RECOMMEND_ESCALATION",
    "HUMAN_APPROVAL_REQUIRED",
}

def supervisor_run(ticket_id: int, goal: str):
    """
    Supervisor decision engine (READ-ONLY)
    - No writes
    - No escalation
    - Only recommendations
    """

    # 1️⃣ Fetch ticket
    try:
        ticket_resp = get_ticket(ticket_id)
        ticket = ticket_resp.get("ticket", {})
    except Exception as e:
        yield {
            "agent": "supervisor",
            "stage": "error",
            "error": str(e)
        }
        return

    # 2️⃣ SLA risk (lazy import)
    try:
        from agents.sla_agent import sla_risk
        sla = sla_risk(ticket)
    except Exception:
        sla = "unknown"

    # 3️⃣ Impact (optional, lazy)
    try:
        from agents.impact_agent import analyze_impact
        impact = analyze_impact(ticket_id)
    except Exception:
        impact = {}

    # 4️⃣ Decision policy (VERY SIMPLE & SAFE)
    if sla in ("critical", "high"):
        decision = "RECOMMEND_ESCALATION"
        reason = "High SLA risk"
    elif impact and impact.get("impacted_tickets"):
        decision = "HUMAN_APPROVAL_REQUIRED"
        reason = "Multiple tickets impacted"
    elif ticket.get("priority") in (1, 2):
        decision = "RECOMMEND_INTERNAL_NOTE"
        reason = "Low priority, informational handling"
    else:
        decision = "WAIT"
        reason = "No immediate action required"

    # 5️⃣ Final decision output (READ-ONLY)
    yield {
        "agent": "supervisor",
        "stage": "decision",
        "ticket_id": ticket_id,
        "goal": goal,
        "sla": sla,
        "impact": impact,
        "decision": decision,
        "reason": reason
    }

    yield {
        "agent": "supervisor",
        "stage": "done"
    }
