import json
from pathlib import Path

DATA = Path("/opt/shix/data/synthetic/kb.json")

def search_kb(query: str):
    kb = json.loads(DATA.read_text())
    q = query.lower()
    return [a for a in kb if q in a["title"].lower() or q in a["content"].lower()]
