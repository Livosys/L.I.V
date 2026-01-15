from mcp.dispatcher import dispatch

def run_mcp_from_message(message):
    result = dispatch("LIST_TICKETS", message)

    return {
        "answer": result.get("answer", ""),
        "sources": result.get("data", [])
    }
