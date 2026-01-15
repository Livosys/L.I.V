import faiss, os, pickle
import numpy as np
from openai import OpenAI

client = OpenAI()
DIM = 1536
PATH = "/opt/shix/data/faiss"
os.makedirs(PATH, exist_ok=True)

index = faiss.IndexFlatL2(DIM)
meta = []

def embed(text):
    r = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(r.data[0].embedding, dtype="float32")

def add(doc):
    v = embed(doc["text"])
    index.add(np.array([v]))
    meta.append(doc)
    save()

def search(q, k=5):
    v = embed(q)
    D, I = index.search(np.array([v]), k)
    return [meta[i] for i in I[0] if i < len(meta)]

def save():
    faiss.write_index(index, f"{PATH}/index.faiss")
    pickle.dump(meta, open(f"{PATH}/meta.pkl","wb"))

def load():
    global index, meta
    if os.path.exists(f"{PATH}/index.faiss"):
        index = faiss.read_index(f"{PATH}/index.faiss")
        meta = pickle.load(open(f"{PATH}/meta.pkl","rb"))
