from backend.agents.correlation_agent import detect_pattern
from backend.agents.problem_agent import link_problem

def process(tickets: list):
    result = detect_pattern(tickets)
    if not result:
        return "no_problem"

    for t in tickets:
        link_problem(t)

    return {
        "status": "problem_created",
        "signature": result["signature"],
        "tickets": [t["id"] for t in tickets]
    }
