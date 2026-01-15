def run_tool(task: str, query: str) -> dict:
    if task == "analyze_ticket":
        return {
            "analysis": "Detta är ett ITSM-ärende som kräver status- och SLA-analys."
        }

    if task == "summarize":
        return {
            "analysis": f"Sammanfattning av frågan: {query}"
        }

    return {
        "analysis": "Allmän rådgivning utan specifika verktyg."
    }
