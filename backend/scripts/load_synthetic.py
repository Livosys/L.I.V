import json

with open("/opt/shix/backend/data/synthetic_tickets.json") as f:
    tickets = json.load(f)

with open("/opt/shix/backend/data/synthetic_intents.json") as f:
    intents = json.load(f)

print(f"Loaded {len(tickets)} synthetic tickets")
print(f"Loaded {len(intents)} synthetic intent examples")
