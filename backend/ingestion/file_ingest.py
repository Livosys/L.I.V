from fastapi import UploadFile
from pypdf import PdfReader
from ingestion.ingest import ingest_text

async def ingest_file_content(file: UploadFile):
    filename = file.filename.lower()
    content = ""

    if filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        for page in reader.pages:
            content += page.extract_text() or ""
    else:
        content = (await file.read()).decode("utf-8")

    doc_id = ingest_text(content)
    return doc_id
