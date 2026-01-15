import json
from pathlib import Path

OUT = Path("/opt/shix/data/synthetic")
OUT.mkdir(parents=True, exist_ok=True)

kb = [
    {
        "id": 1,
        "title": "Felsök VPN-problem",
        "content": "Starta om VPN-klienten, kontrollera MFA och testa annan anslutning."
    },
    {
        "id": 2,
        "title": "Återställ lösenord",
        "content": "Gå till lösenordsportalen och följ instruktionerna."
    },
    {
        "id": 3,
        "title": "Begär server access",
        "content": "Skapa ett ärende och ange servernamn och behörighet."
    },
    {
        "id": 4,
        "title": "Outlook kraschar",
        "content": "Rensa cache och uppdatera Office."
    },
]

with open(OUT / "kb.json", "w") as f:
    json.dump(kb, f, ensure_ascii=False, indent=2)

print("✅ Synthetic KB skapad:", OUT / "kb.json")
