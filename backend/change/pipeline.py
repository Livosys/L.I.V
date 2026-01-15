from change.history import analyze_change_history
from change.dependencies import get_affected_services
from change.risk_engine import calculate_risk
from change.impact_prediction import predict_impact

def predict_change_impact(change, past_tickets):
    history = analyze_change_history(change, past_tickets)
    dependencies = get_affected_services(change.service)

    risk = calculate_risk(change, history, dependencies)
    impact = predict_impact(risk)

    return {
        "risk": risk,
        "impact": impact,
        "affected_services": dependencies,
        "history": history
    }
