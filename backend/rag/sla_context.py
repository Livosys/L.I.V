def apply_sla_weighting(query: str, contexts: list[str]) -> list[str]:
    """
    Prioritera kontext baserat på SLA-känslighet.
    """
    critical_keywords = ["vpn", "network", "email", "outage", "login"]

    high = []
    normal = []

    for c in contexts:
        if any(k in c.lower() for k in critical_keywords):
            high.append(c)
        else:
            normal.append(c)

    return high + normal
