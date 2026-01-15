def generate_kb_suggestion(query: str, lang: str) -> dict:
    if lang == "sv":
        return {
            "suggestion": "Det finns ingen artikel ännu.",
            "proposed_title": f"Guide: {query}",
            "proposed_sections": [
                "Syfte",
                "Förutsättningar",
                "Steg-för-steg",
                "Felsökning"
            ]
        }

    return {
        "suggestion": "No article exists yet.",
        "proposed_title": f"Guide: {query}",
        "proposed_sections": [
            "Purpose",
            "Prerequisites",
            "Step-by-step",
            "Troubleshooting"
        ]
    }
