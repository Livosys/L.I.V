import json
import re
from pathlib import Path
from difflib import SequenceMatcher

DATA = Path("/opt/shix/backend/data/intent_dataset.json")
INTENTS = json.loads(DATA.read_text())

def score(a, b):
    return SequenceMatcher(None, a, b).ratio()

def resolve(text: str):
    t = text.lower().strip()

    filters = {
        "keyword": None,
        "status": None,
        "mine": False
    }

    if "vpn" in t:
        filters["keyword"] = "vpn"

    if "pågående" in t or "öppna" in t:
        filters["status"] = "open"

    if "mina" in t:
        filters["mine"] = True

    if re.search(r"\b\d+\b", t) and "ärend" in t:
        return {"intent": "OPEN_TICKET", "filters": filters}

    best = ("UNKNOWN", 0.0)
    for row in INTENTS:
        s = score(t, row["text"])
        if s > best[1]:
            best = (row["intent"], s)

    return {
        "intent": best[0] if best[1] >= 0.5 else "UNKNOWN",
        "filters": filters
    }
