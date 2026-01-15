def require_role(user_role: str, allowed: list[str]):
    if user_role not in allowed:
        raise PermissionError("Access denied")
