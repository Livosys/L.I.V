import re

def detect(message: str):
    m = message.lower().strip()

    if m in ["hjälp", "help"]:
        return {"intent": "HELP", "params": {}}

    if m in ["visa ärenden", "lista ärenden"]:
        return {"intent": "LIST_TICKETS", "params": {}}

    if m in ["visa kb", "lista kb"]:
        return {"intent": "LIST_KB", "params": {}}

    if m.startswith("sök kb"):
        return {"intent": "SEARCH_KB", "params": {"query": m.replace("sök kb", "").strip()}}

    if m.startswith("status"):
        return {"intent": "TICKET_META", "params": {"id": int(m.split()[-1])}}

    if re.match(r"(öppna|visa)\s+\d+", m):
        return {"intent": "OPEN_TICKET", "params": {"id": int(m.split()[-1])}}

    return {"intent": "RAG", "params": {"query": message}}
