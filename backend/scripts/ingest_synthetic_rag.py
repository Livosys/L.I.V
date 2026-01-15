import json
from pathlib import Path
from rag.vector_store import VectorStore

BASE = Path("/opt/shix/data/synthetic")
vs = VectorStore("/opt/shix/data/vectors")

docs = []

for p in ["tickets.json", "kb.json"]:
    data = json.loads((BASE / p).read_text())
    for item in data:
        text = " ".join([str(v) for v in item.values()])
        docs.append(text)

vs.add_texts(docs)
vs.save()

print("✅ Synthetic data indexerad i RAG")
