from typing import Iterator
from rag.answer_engine import answer_query
import json
import time

def stream_answer(q: str) -> Iterator[str]:
    res = answer_query(q)
    for ch in res.get("answer", ""):
        yield f"data: {json.dumps({'token': ch})}\n\n"
        time.sleep(0.01)
    yield "data: [DONE]\n\n"
