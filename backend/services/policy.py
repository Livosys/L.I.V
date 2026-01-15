def allow_apply(ticket: dict, user_role: str):
    if ticket.get("priority") == 4 and user_role != "admin":
        return False
    return True
