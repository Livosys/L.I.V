def auto_propose(text: str):
    t = text.lower()
    if "vpn" in t:
        return "AI suggestion: reset VPN profile and clear cache."
    if "email" in t:
        return "AI suggestion: re-sync mailbox and reset password."
    if "printer" in t:
        return "AI suggestion: reinstall printer driver."
    return None
