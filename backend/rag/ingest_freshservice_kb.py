import json
from pathlib import Path

# --- MOCK KB INGEST (TRIAL SAFE) ---
# This bypasses Freshservice Solutions API completely.
# Replace this file later when Enterprise license is active.

MOCK_KB_PATH = Path(__file__).parent / "mock_kb.json"


def ingest():
    if not MOCK_KB_PATH.exists():
        print("[ERROR] mock_kb.json not found")
        return

    with open(MOCK_KB_PATH, "r") as f:
        documents = json.load(f)

    if not documents:
        print("No KB articles found")
        return

    print(f"Loaded {len(documents)} KB articles")

    # ---- SIMULATED VECTOR INGEST ----
    # Replace with real embedding/store logic if needed
    for doc in documents:
        print(f"Ingesting: {doc['title']}")

    print("Mock KB ingest completed successfully")


if __name__ == "__main__":
    ingest()
