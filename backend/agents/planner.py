def plan(user_goal: str):
    steps = []
    if "sammanfatta" in user_goal.lower():
        steps.append("get_ticket")
        steps.append("rag")
    if "eskalera" in user_goal.lower():
        steps.append("sla")
        steps.append("escalate")
    steps.append("respond")
    return steps
