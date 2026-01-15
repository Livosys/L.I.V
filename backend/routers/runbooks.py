from fastapi import APIRouter
from runbooks.registry import find_runbook
from runbooks.policy import allow_auto_execute
from runbooks.executor import execute_runbook

router = APIRouter()

@router.post("/api/runbooks/execute")
def run(ticket_id: int, root_cause: str, ctx: dict):
    rb = find_runbook(root_cause)
    if not rb:
        return {"status": "no_runbook"}

    if not allow_auto_execute(rb, ctx):
        return {"status": "approval_required"}

    result = execute_runbook(rb, ticket_id)
    return {"status": "executed", "result": result}
