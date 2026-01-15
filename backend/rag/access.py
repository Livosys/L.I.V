ROLE_ACCESS = {
    "user": {"policy"},
    "it": {"policy", "manual", "kb"},
    "admin": {"policy", "manual", "kb", "ticket"},
}

def allowed_sources(role: str) -> set[str]:
    return ROLE_ACCESS.get(role, {"policy"})
