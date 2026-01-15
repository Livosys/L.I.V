import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "synthetic.json"

def load_synthetic():
    if not DATA_PATH.exists():
        return []
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))
