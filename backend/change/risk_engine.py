class RiskEngine:
    def simulate(self, change):
        return {
            "risk": {
                "risk_level": "HIGH",
                "risk_score": 87,
                "reasons": [
                    "Emergency change",
                    "Historical incidents",
                    "Multiple dependencies"
                ]
            },
            "impact": {
                "sla_risk": "high",
                "mi_probability": 0.62,
                "recommendation": "Start war-room and schedule off-hours"
            },
            "affected_services": ["VPN", "Auth", "Network"],
            "customer_impact": {
                "estimated_users_affected": 120
            }
        }

risk_engine = RiskEngine()
