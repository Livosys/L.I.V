from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import json, time

from agents.supervisor import run_supervisor_stream

router = APIRouter(
    prefix="/api",
    tags=["Supervisor-Stream"]
)

class StreamRequest(BaseModel):
    ticket_id: int
    goal: str

def event_stream(steps):
    for step in steps:
        yield f"data: {json.dumps(step)}\n\n"
        time.sleep(0.4)
    yield "data: [DONE]\n\n"

@router.get("/react/stream/{ticket_id}")
def react_stream(ticket_id: int, goal: str):
    steps = run_supervisor_stream(ticket_id=ticket_id, goal=goal)
    return StreamingResponse(
        event_stream(steps),
        media_type="text/event-stream"
    )
