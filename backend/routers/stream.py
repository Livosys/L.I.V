from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import json
import time

from backend.agents.supervisor import supervisor_run

router = APIRouter(prefix="/api/stream", tags=["stream"])

def sse_event(event: str, data: dict):
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"

@router.post("")
def stream(payload: dict):
    ticket_id = payload.get("ticket_id")
    goal = payload.get("goal")

    def generator():
        yield sse_event("status", {"message": "Supervisor started"})

        for step in supervisor_run(ticket_id, goal):
            yield sse_event(step["type"], step["data"])
            time.sleep(0.2)

        yield sse_event("final", {"done": True})

    return StreamingResponse(generator(), media_type="text/event-stream")
