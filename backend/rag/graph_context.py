def enrich(query: str) -> dict:
    return {
        "relations": [
            "Ticket → SLA",
            "Ticket → Category",
            "Ticket → Assigned Agent"
        ],
        "note": "Graph-kontext applicerad"
    }
