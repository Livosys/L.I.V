TOOLS = {
    "HELP": {},
    "ECHO": {"message": "string"},
    "RAG_SEARCH": {"query": "string"},

    "LIST_TICKETS": {},
    "OPEN_TICKET": {"id": "int"},

    "TICKET_META": {"id": "int"},

    "LIST_KB": {},
    "SEARCH_KB": {"query": "string"},
}

def is_tool_allowed(name: str) -> bool:
    return name in TOOLS
