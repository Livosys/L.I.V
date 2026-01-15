def should_create_problem(tickets: list):
    if len(tickets) >= 5:
        return True, {
            "reason": "Recurring incidents",
            "ticket_ids": [t["id"] for t in tickets]
        }
    return False, None
