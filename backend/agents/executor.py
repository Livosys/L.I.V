from agents.tools import tool_get_ticket, tool_sla, tool_rag

def execute_tools(context: dict):
    results = {}

    if "ticket_id" in context:
        results["ticket"] = tool_get_ticket(context["ticket_id"])

    results["sla"] = tool_sla(context)
    results["rag"] = tool_rag(context)

    return results
