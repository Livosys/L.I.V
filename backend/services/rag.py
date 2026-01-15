import services.freshservice as fs

def answer_from_knowledge(question: str):
    data = fs.my_tickets()
    tickets = data.get("tickets", [])

    for t in tickets:
        desc = (t.get("description_text") or "").lower()
        if any(word in desc for word in question.lower().split()):
            return f"Liknande ärende #{t['id']}: {t.get('subject','')}"

    return None
