def generate_followup(intent: str) -> str | None:
    if intent == "ticket_specific":
        return (
            "Jag hittar inget sådant ärende just nu. "
            "Vill du kontrollera ärendenumret eller vill du se dina senaste ärenden?"
        )

    if intent == "kb_search":
        return (
            "Vill du förtydliga lite? "
            "Gäller detta VPN hemma, på kontoret eller via fjärranslutning?"
        )

    if intent == "general_rag":
        return (
            "Kan du ge lite mer detaljer så att jag kan hjälpa dig bättre?"
        )

    return None
