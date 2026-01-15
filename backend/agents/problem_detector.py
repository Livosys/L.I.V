def detect_problem(tickets: list):
    subjects = {}
    for t in tickets:
        s = t.get("subject")
        subjects.setdefault(s, []).append(t["id"])

    for s, ids in subjects.items():
        if len(ids) >= 3:
            return {"problem": s, "tickets": ids}

    return None
