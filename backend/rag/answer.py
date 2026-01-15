def build_answer(message: str, kb_articles: list, tickets: list | None = None):
    msg = message.lower().strip()

    # 1️⃣ Hälsningar
    if msg in ["hej", "hej!", "hello", "hi", "tjena"]:
        return (
            "Hej! 👋 Jag är L.I.V – din digitala IT-assistent. "
            "Jag kan hjälpa dig att hitta kunskapsartiklar, "
            "se dina ärenden och guida dig steg för steg."
        )

    # 2️⃣ Vad gör du?
    if "vad gör du" in msg or "who are you" in msg:
        return (
            "Jag hjälper dig med IT-support genom att:\n"
            "• hitta relevanta kunskapsartiklar\n"
            "• visa dina ärenden\n"
            "• guida dig steg för steg\n\n"
            "Prova till exempel att skriva: *vpn*, *mina ärenden* eller *installera outlook*."
        )

    # 3️⃣ Kunskapsartiklar hittades
    if kb_articles:
        return (
            f"Jag hittade {len(kb_articles)} relevanta "
            f"kunskapsartikel(ar) baserat på din fråga."
        )

    # 4️⃣ Ärenden hittades
    if tickets:
        return (
            f"Jag hittade {len(tickets)} ärende(n) som är kopplade till dig."
        )

    # 5️⃣ Fallback
    return (
        "Jag är inte helt säker på vad du menar ännu, "
        "men du kan prova att omformulera din fråga eller "
        "söka på ett ämne, till exempel *vpn* eller *e-post*."
    )
