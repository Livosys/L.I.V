SERVICE_DEPENDENCIES = {
    "VPN": ["Auth", "Network", "Firewall"],
    "Email": ["Auth", "DNS"],
    "ERP": ["Database", "Network", "Auth"]
}

def get_affected_services(service: str):
    return SERVICE_DEPENDENCIES.get(service, [])
