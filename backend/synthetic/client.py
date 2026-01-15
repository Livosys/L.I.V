import json
from pathlib import Path

BASE = Path("/opt/shix/backend/synthetic")

def load_tickets():
    with open(BASE / "tickets.json") as f:
        return json.load(f)

def load_kb():
    with open(BASE / "kb.json") as f:
        return json.load(f)
