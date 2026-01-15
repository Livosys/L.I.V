import re
import services.freshservice as fs

INDEX = []

def _chunks(text, size=400):
    words = text.split()
    for i in range(0, len(words), size):
        yield " ".join(words[i:i+size])

def build_index():
    global INDEX
    INDEX = []
    data = fs.my_tickets()
    for t in data.get("tickets", []):
        text = " ".join([
            t.get("subject",""),
            t.get("description_text","")
        ])
        for c in _chunks(text):
            INDEX.append({"ticket_id": t.get("id"), "text": c.lower()})

def search(q: str):
    q = q.lower()
    hits = [x for x in INDEX if all(w in x["text"] for w in q.split())]
    return hits[:3]
