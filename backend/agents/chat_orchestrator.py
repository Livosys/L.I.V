from agents.intent_router import route_intents
from ai.vpn_guide import generate_vpn_guide
from ai.kb_agent import fetch_kb_articles

async def handle_chat(message: str):
    intents = route_intents(message)
    response = {}

    # 📚 Kunskapsbas (FAILSAFE)
    if "kb" in intents:
        try:
            articles = fetch_kb_articles(message)
            if articles:
                response["answer"] = f"Jag hittade {len(articles)} artiklar som matchar din fråga."
                response["articles"] = articles
        except Exception as e:
            # ❗ Isolera Freshservice-fel
            response["kb_error"] = "Kunskapsbasen är tillfälligt otillgänglig."

    # 🔐 VPN-guide (ALLTID TILLÅTEN)
    if "vpn" in message.lower():
        guide = generate_vpn_guide()
        response.setdefault("answer", guide["answer"])
        response["steps"] = guide["steps"]

    # 🎫 Ärenden
    if "tickets" in intents:
        response.setdefault(
            "answer",
            "Jag har hittat information kopplat till dina ärenden."
        )
        response["action"] = "FETCH_MY_TICKETS"

    # 🧠 Fallback (ALDRIG TOMT)
    if not response:
        response["answer"] = (
            "Jag kan hjälpa dig med:\n"
            "• Dina ärenden\n"
            "• Söka i kunskapsbasen\n"
            "• Steg-för-steg guider\n\n"
            "Prova t.ex:\n"
            "• mina ärenden\n"
            "• visa mig vpn artikel\n"
            "• vpn"
        )

    return response
