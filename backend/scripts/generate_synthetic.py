import json
import random

TITLES = [
    "VPN fungerar inte",
    "Server access",
    "E-post synkar inte",
    "Adobe Illustrator licens",
    "WiFi långsamt",
    "Kan inte logga in",
    "MFA problem",
    "Skrivare offline",
    "Teams kraschar",
    "Lösenordsbyte"
]

STATUSES = ["Open", "In Progress", "Pending", "Resolved"]
PRIORITIES = ["Low", "Medium", "High"]
CATEGORIES = ["Network", "Access", "Email", "Software", "Hardware"]

tickets = []
for i in range(1, 101):
    tickets.append({
        "id": i,
        "title": random.choice(TITLES),
        "description": "Synthetic ticket for training/testing",
        "status": random.choice(STATUSES),
        "priority": random.choice(PRIORITIES),
        "category": random.choice(CATEGORIES)
    })

with open("/opt/shix/backend/data/synthetic_tickets.json", "w") as f:
    json.dump(tickets, f, indent=2)

print("Generated 100 synthetic tickets")
