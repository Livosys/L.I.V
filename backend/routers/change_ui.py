from fastapi import APIRouter
from change.pipeline import predict_change_impact
from change.model import ChangeRequest
from audit.audit_log import log_action

router = APIRouter()

@router.post("/api/change/simulate")
def simulate_change(payload: dict):
    change = ChangeRequest(**payload["change"])
    past_tickets = payload.get("past_tickets", [])

    result = predict_change_impact(change, past_tickets)

    log_action(
        action="CHANGE_SIMULATED_UI",
        ticket_id=0,
        actor="ui",
        payload={
            "change_id": change.id,
            "risk": result["risk"]
        }
    )

    return result
