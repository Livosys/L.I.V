def predict_impact(risk: dict):
    if risk["risk_level"] == "high":
        return {
            "sla_risk": "high",
            "mi_probability": 0.6,
            "recommendation": "Schedule outside business hours + full war-room"
        }

    if risk["risk_level"] == "medium":
        return {
            "sla_risk": "medium",
            "mi_probability": 0.3,
            "recommendation": "Add extra monitoring and rollback plan"
        }

    return {
        "sla_risk": "low",
        "mi_probability": 0.1,
        "recommendation": "Proceed with standard approval"
    }
