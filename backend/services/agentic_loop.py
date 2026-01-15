class AgenticLoop:
    def run(self, ticket_context):
        return {
            "decision": "HUMAN_APPROVAL_REQUIRED",
            "confidence": 0.86,
            "allowed_actions": [
                "Add private note",
                "Suggest KB article",
                "Escalate to network team"
            ]
        }
