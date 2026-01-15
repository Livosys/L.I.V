from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import time

router = APIRouter(prefix="/api", tags=["RAG-STREAM"])

class RagPayload(BaseModel):
    query: str

@router.post("/rag/stream")
def rag_stream(payload: RagPayload):

    def event_generator():
        chunks = [
            "Analyserar frågan...\n",
            "Identifierar ärendetyp...\n",
            "Applicerar ITSM-logik...\n",
            "Genererar svar...\n",
            "Klart.\n"
        ]
        for c in chunks:
            yield f"data: {c}\n\n"
            time.sleep(0.6)

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
