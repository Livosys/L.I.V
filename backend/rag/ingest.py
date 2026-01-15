import json

KB = [
    {
        "id": 1,
        "title": "VPN fungerar inte",
        "content": "Kontrollera att VPN-klienten är uppdaterad och MFA fungerar."
    },
    {
        "id": 2,
        "title": "Lösenord återställning",
        "content": "Återställ lösenord via Azure AD portalen."
    }
]

with open("/opt/shix/backend/rag/store.json", "w") as f:
    json.dump(KB, f)
