def respond(task: str, tool_result: dict) -> str:
    if task == "analyze_ticket":
        return f"""
🧠 Agent-analys:
{tool_result['analysis']}

Rekommendation:
Verifiera ärendets prioritet och nuvarande SLA.
""".strip()

    if task == "summarize":
        return tool_result["analysis"]

    return "Jag har analyserat din fråga och kan hjälpa dig vidare."
