import json
from pathlib import Path
import random

OUT = Path("/opt/shix/data/synthetic")
OUT.mkdir(parents=True, exist_ok=True)

subjects = [
    "VPN fungerar inte",
    "Kan inte logga in",
    "Behöver server access",
    "Outlook kraschar",
    "WiFi långsamt",
    "Adobe Illustrator licens",
    "Glömt lösenord",
    "Ny användare onboarding",
]

descriptions = [
    "Användaren rapporterar problem sedan imorse.",
    "Felet uppstår efter uppdatering.",
    "Gäller flera användare.",
    "Endast på distans.",
    "Fungerade igår.",
]

tickets = []
for i in range(1, 51):
    tickets.append({
        "id": i,
        "subject": random.choice(subjects),
        "description": random.choice(descriptions),
        "status": random.choice(["open", "pending", "resolved"]),
        "priority": random.choice(["low", "medium", "high"]),
    })

with open(OUT / "tickets.json", "w") as f:
    json.dump(tickets, f, ensure_ascii=False, indent=2)

print("✅ Synthetic tickets skapade:", OUT / "tickets.json")
