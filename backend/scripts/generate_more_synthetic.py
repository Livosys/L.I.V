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
    "Lösenordsbyte",
    "SharePoint åtkomst",
    "OneDrive synkfel",
    "Citrix startar inte",
    "Zoom ljudproblem",
    "Nätverksdropouts"
]

STATUSES = ["Open", "In Progress", "Pending", "Resolved"]
PRIORITIES = ["Low", "Medium", "High"]
CATEGORIES = ["Network", "Access", "Email", "Software", "Hardware", "Collaboration"]

tickets = []
TOTAL = 500  # ÄNDRA HÄR om du vill ha fler (t.ex. 1000, 5000)

for i in range(1, TOTAL + 1):
    tickets.append({
        "id": i,
        "title": random.choice(TITLES),
        "description": "Synthetic ticket generated for training/testing",
        "status": random.choice(STATUSES),
        "priority": random.choice(PRIORITIES),
        "category": random.choice(CATEGORIES)
    })

with open("/opt/shix/backend/data/synthetic_tickets.json", "w") as f:
    json.dump(tickets, f, indent=2)

print(f"Generated {TOTAL} synthetic tickets")
