def forecast_customer_impact(past_tickets: list):
    users = set()

    for t in past_tickets:
        if t.get("requester_email"):
            users.add(t["requester_email"])

    return {
        "estimated_users_affected": len(users),
        "confidence": min(0.3 + len(users) * 0.05, 0.9)
    }
