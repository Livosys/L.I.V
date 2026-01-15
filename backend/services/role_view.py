def filter_by_role(data: dict, role: str):
    if role == "user":
        return {
            "ticket": {
                "id": data["ticket"]["id"],
                "subject": data["ticket"]["subject"],
                "status": data["ticket"]["status"]
            }
        }

    if role == "manager":
        return {
            "ticket": data["ticket"],
            "sla": data["sla"]
        }

    # agent / admin
    return data
