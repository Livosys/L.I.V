TRADEMARK = "SHIX™ — Designed & Trademarked by Liv. Dawod"

ROLE_MAP = {
    "SHIX-Users": "user",
    "SHIX-Agents": "agent",
    "SHIX-Admins": "admin"
}

PERMISSIONS = {
    "user": ["chat"],
    "agent": ["chat", "resolve"],
    "admin": ["chat", "resolve", "admin"]
}

def role_from_claims(claims):
    groups = claims.get("groups", [])
    for g in groups:
        if g in ROLE_MAP:
            return ROLE_MAP[g]
    return "user"

def has_permission(role, permission):
    return permission in PERMISSIONS.get(role, [])
