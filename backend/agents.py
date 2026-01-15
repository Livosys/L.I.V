AGENTS = {
    "L1": "Handle basic issues and FAQs",
    "L2": "Handle technical troubleshooting",
    "L3": "Handle deep system issues"
}

def route_agent(issue_type):
    if issue_type in ["password", "vpn"]:
        return "L1"
    if issue_type in ["email", "network"]:
        return "L2"
    return "L3"
