import os

TOKENS = {
    os.getenv("ADMIN_TOKEN", "ADMIN_TOKEN_123"): "admin",
    os.getenv("USER_TOKEN", "USER_TOKEN_123"): "user"
}

def get_role(token: str | None):
    if not token:
        return None
    return TOKENS.get(token)
