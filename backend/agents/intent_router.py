import re

def normalize(text: str) -> str:
    t = text.lower().strip()

    replacements = {
        "isa": "visa",
        "viska": "visa",
        "visaa": "visa",
        "minna": "mina",
        "ärendne": "ärenden",
        "arenden": "ärenden",
        "kunskabasen": "kunskapsbasen",
        "kb": "kunskapsbas",
    }

    for wrong, correct in replacements.items():
        t = re.sub(rf"\b{wrong}\b", correct, t)

    return t


def route_intents(message: str) -> list[str]:
    m = normalize(message)
    intents = []

    # 👋 Hälsning
    if m in ["hej", "hallå", "hi", "hello", "tjena"]:
        return ["greeting"]

    # 🙂 Smalltalk
    if any(k in m for k in ["hur mår du", "läget", "hur ar du"]):
        intents.append("smalltalk")

    # ✅ Bekräftelse
    if m in ["ok", "okej", "ja", "yes", "gör det"]:
        intents.append("confirm")

    # 🎫 Ärenden
    if "mina ärenden" in m:
        intents.append("tickets")

    # 📚 ALLA KB-ARTIKLAR (DETTA VAR SAKNAT)
    if any(k in m for k in [
        "visa mig kunskapsbas artiklar",
        "visa mig kb artiklar",
        "visa kb artiklar",
        "kb artiklar",
        "alla kb artiklar",
        "alla artiklar",
        "visa kunskapsbasen",
    ]):
        intents.append("kb_all")

    # 📚 VPN-artiklar
    if "vpn" in m:
        intents.append("kb_vpn")

    return intents
