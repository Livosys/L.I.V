import os
from rag.chunker import smart_chunk

def load_documents(base_path):
    chunks = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".txt"):
                continue

            path = os.path.join(root, file)
            category = os.path.basename(os.path.dirname(path))

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            doc_chunks = smart_chunk(text, file)
            for c in doc_chunks:
                c["category"] = category
            chunks.extend(doc_chunks)

    return chunks
