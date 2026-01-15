import os
import pickle
import faiss
import numpy as np
from openai import OpenAI
from freshservice.ticket_client import list_tickets, get_ticket_by_id

DATA_DIR = "/opt/shix/data/vectors"
INDEX_PATH = os.path.join(DATA_DIR, "index.faiss")
META_PATH = os.path.join(DATA_DIR, "meta.pkl")

client = OpenAI()

os.makedirs(DATA_DIR, exist_ok=True)

def embed(text: str):
    resp = client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    return np.array(resp.data[0].embedding, dtype="float32")

def ingest():
    tickets = list_tickets(limit=50)
    if not tickets:
        print("No tickets to ingest")
        return

    vectors = []
    meta = []

    for t in tickets:
        full = get_ticket_by_id(str(t["id"]))
        text = f"{full['subject']}\n{full.get('description','')}"
        vec = embed(text)

        vectors.append(vec)
        meta.append({
            "type": "ticket",
            "id": full["id"],
            "title": full["subject"],
            "url": f"https://livosys.freshservice.com/a/tickets/{full['id']}",
            "explain": ["server", "access", "permission"]  # baseline
        })

    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))

    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(meta, f)

    print(f"✅ Indexed {len(meta)} tickets into RAG")

if __name__ == "__main__":
    ingest()
