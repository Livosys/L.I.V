def present_change_impact(change_id, result, war_room_started):
    return {
        "ui_type": "card_expand",
        "card": {
            "title": f"Change CHG-{change_id}",
            "badges": {
                "risk": result["risk"]["risk_level"],
                "sla": result["impact"]["sla_risk"],
                "mi": f'{int(result["impact"]["mi_probability"] * 100)}%'
            },
            "summary": {
                "users_affected": result.get("customer_impact", {}).get("estimated_users_affected"),
                "war_room": war_room_started
            }
        },
        "expand": {
            "risk_score": result["risk"]["risk_score"],
            "reasons": result["risk"]["reasons"],
            "affected_services": result["affected_services"],
            "recommendation": result["impact"]["recommendation"]
        }
    }
