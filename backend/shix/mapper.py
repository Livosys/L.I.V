from html.parser import HTMLParser

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, d):
        self.text.append(d)

    def get_data(self):
        return " ".join(self.text)

def html_to_text(html: str | None) -> str:
    if not html:
        return ""
    s = HTMLStripper()
    s.feed(html)
    return s.get_data()

def map_ticket(raw: dict) -> dict:
    t = raw.get("ticket", raw)

    return {
        "ticket_id": t.get("id"),
        "title": t.get("subject"),
        "description": html_to_text(t.get("description")),
        "status": t.get("status"),
        "priority": t.get("priority"),
        "created_at": t.get("created_at"),
        "updated_at": t.get("updated_at"),
        "requester_id": t.get("requester_id"),
        "agent_id": t.get("assigned_agent_id"),
        "tags": t.get("tags", [])
    }
