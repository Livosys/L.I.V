def can(role: str, action: str) -> bool:
    rules = {
        "end_user": ["read"],
        "agent": ["read", "suggest"],
        "admin": ["read", "suggest", "approve", "write"]
    }
    return action in rules.get(role, [])

def require(role: str, action: str):
    if not can(role, action):
        raise PermissionError(f"Role {role} cannot perform {action}")
