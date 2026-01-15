from services.vector_store import add_documents
from services.freshservice_reader import get_all_tickets, get_all_kb

docs = []
sources = []

for t in get_all_tickets(limit=500):
    docs.append(f"{t['subject']} {t['description_text']}")
    sources.append({"type": "ticket", "id": t["id"]})

for kb in get_all_kb(limit=500):
    docs.append(f"{kb['title']} {kb.get('description_text','')}")
    sources.append({"type": "kb", "id": kb["id"]})

add_documents(docs, sources)
print("✅ RAG INGEST COMPLETE")
