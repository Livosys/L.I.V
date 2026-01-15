from services.sla_risk import sla_risk_level

def should_escalate(ctx: dict):
    sla = ctx.get("sla")
    risk = sla_risk_level(sla)

    vip = ctx.get("requester", {}).get("vip", False)
    priority = ctx["ticket"].get("priority")

    if risk in ["critical", "breached"]:
        return True, "SLA risk"

    if vip and priority in [1, 2]:
        return True, "VIP user with high priority"

    return False, None
