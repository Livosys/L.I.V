def reflect(context: dict):
    notes = []
    if context.get("sla") == "critical":
        notes.append("Akut SLA – omedelbar åtgärd")
    if "rag" in context:
        notes.append("KB-baserad rekommendation tillämpad")
    return notes
