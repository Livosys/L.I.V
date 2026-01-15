import os
from pathlib import Path
from docling.document_converter import DocumentConverter

from rag.vector_store import add_texts

DOCUMENT_ROOT = Path("/opt/shix/backend/documents")

def infer_doc_type(path: Path) -> str:
    parts = path.parts
    if "policies" in parts:
        return "policy"
    if "manuals" in parts:
        return "manual"
    return "document"

def load_documents():
    docs = []
    converter = DocumentConverter()

    for path in DOCUMENT_ROOT.rglob("*"):
        if path.suffix.lower() not in [".pdf", ".docx", ".pptx"]:
            continue

        print(f"[DOC] Processing {path}")

        result = converter.convert(str(path))
        document = result.document
        doc_type = infer_doc_type(path)

        for section in document.sections:
            text = section.text.strip()
            if not text or len(text) < 50:
                continue

            meta = {
                "source": "document",
                "doc_type": doc_type,
                "file": path.name,
                "path": str(path.relative_to(DOCUMENT_ROOT)),
                "section": section.heading or "N/A",
                "page": section.page_numbers[0] if section.page_numbers else None,
            }

            docs.append((text, meta))

    return docs

def ingest():
    docs = load_documents()
    if not docs:
        print("No documents found")
        return

    texts = [d[0] for d in docs]
    metas = [d[1] for d in docs]

    add_texts(texts, metas)
    print(f"Ingested {len(texts)} document chunks")

if __name__ == "__main__":
    ingest()
