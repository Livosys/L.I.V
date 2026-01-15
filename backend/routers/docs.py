from fastapi import APIRouter
from pathlib import Path
import time

router = APIRouter(prefix="/api/docs", tags=["docs"])

DOC_ROOT = Path("/opt/shix/backend/documents")

@router.get("/status")
def docs_status():
    files = []
    for p in DOC_ROOT.rglob("*"):
        if p.suffix.lower() in [".pdf", ".docx", ".pptx"]:
            files.append(p)

    stats = {
        "total_documents": len(files),
        "policies": len([f for f in files if "policies" in f.parts]),
        "manuals": len([f for f in files if "manuals" in f.parts]),
        "last_modified": max(
            (f.stat().st_mtime for f in files),
            default=None
        ),
    }

    if stats["last_modified"]:
        stats["last_modified"] = time.strftime(
            "%Y-%m-%d %H:%M:%S",
            time.localtime(stats["last_modified"])
        )

    return stats
from fastapi.responses import FileResponse

@router.get("/file/{filename}")
def get_document(filename: str):
    path = DOC_ROOT / "policies" / filename
    if not path.exists():
        return {"error": "File not found"}
    return FileResponse(path)
