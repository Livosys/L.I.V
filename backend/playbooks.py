PLAYBOOKS = [
    {
        "if": {"category": "VPN"},
        "then": "reset_vpn"
    },
    {
        "if": {"category": "Email"},
        "then": "clear_mailbox"
    }
]

def match_playbook(ticket):
    for p in PLAYBOOKS:
        if p["if"].get("category") == ticket.get("category"):
            return p["then"]
    return None
