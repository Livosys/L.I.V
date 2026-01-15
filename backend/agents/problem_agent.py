from backend.freshservice.writeback import add_note

def link_problem(ticket: dict):
    add_note(ticket["id"], "🧩 Kopplad till Problem Record p.g.a. mönster.", True)
    return "problem_linked"
