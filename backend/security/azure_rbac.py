def roles_from_token(token_payload):
    return token_payload.get("roles", [])

def can_access(category, roles):
    if "KB_ADMIN" in roles:
        return True
    if category == "HR" and "HR" in roles:
        return True
    if category != "HR":
        return True
    return False
