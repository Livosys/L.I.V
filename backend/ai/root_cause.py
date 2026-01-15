def analyze_root_cause(ctx: dict):
    text = (
        ctx["ticket"].get("description", "") +
        " " +
        (ctx.get("last_public_reply") or {}).get("body_text", "")
    ).lower()

    causes = []

    if "vpn" in text and "timeout" in text:
        causes.append(("VPN gateway timeout", 0.82))

    if "access" in text and "permission" in text:
        causes.append(("Access rights misconfiguration", 0.76))

    if "server" in text and "down" in text:
        causes.append(("Server unavailable", 0.88))

    if not causes:
        return {
            "root_cause": "Unknown – needs manual investigation",
            "likelihood": 0.40
        }

    best = max(causes, key=lambda x: x[1])
    return {
        "root_cause": best[0],
        "likelihood": best[1]
    }
