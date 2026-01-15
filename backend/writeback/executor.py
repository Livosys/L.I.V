from ai.writeback_text import generate_note
from freshservice.write_note import add_private_note

def execute_approved(ticket_id: int, summary: str):
    body = generate_note(summary)
    result = add_private_note(ticket_id, body)
    return {"status":"ok","note":body,"fs_result":result}
