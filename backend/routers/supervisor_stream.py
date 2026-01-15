from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from agents.supervisor import run_supervisor_stream
import json

router = APIRouter(prefix="/api/supervisor", tags=["supervisor"])

@router.post("/stream")
def supervisor_stream(payload: dict):
    def event_generator():
        for event in run_supervisor_stream(**payload):
            yield f"data: {json.dumps(event)}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
