POLICIES = {
    "default": {
        "allow_writeback": False,
        "allow_escalation": False
    },
    "enterprise": {
        "allow_writeback": True,
        "allow_escalation": True
    }
}

def check_policy(tenant: str, action: str) -> bool:
    policy = POLICIES.get(tenant, POLICIES["default"])
    return policy.get(action, False)
