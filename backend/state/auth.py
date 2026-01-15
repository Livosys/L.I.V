from fastapi import Request

ROLE_MAP = {
    "requester": "user",
    "agent": "it",
    "admin": "admin",
}

def get_user_role(request: Request) -> str:
    # Från Freshservice proxy / framtida SSO
    fs_role = request.headers.get("X-Freshservice-Role")
    if fs_role:
        return ROLE_MAP.get(fs_role.lower(), "user")

    # Fallback
    return "user"
