import json
from pathlib import Path
import itertools

OUT = Path("/opt/shix/backend/data")
OUT.mkdir(parents=True, exist_ok=True)

intents = []

# 🔹 LIST_TICKETS
list_templates = [
    "visa {}",
    "visa alla {}",
    "lista {}",
    "visa mig {}",
    "kan du visa {}",
    "jag vill se {}",
]
ticket_words = ["ärenden", "tickets", "supportärenden"]

for t, w in itertools.product(list_templates, ticket_words):
    intents.append({"text": t.format(w), "intent": "LIST_TICKETS"})

# 🔹 COUNT_TICKETS
count_templates = [
    "hur många {} finns",
    "antal {}",
    "hur många {} har jag",
]
for t, w in itertools.product(count_templates, ticket_words):
    intents.append({"text": t.format(w), "intent": "COUNT_TICKETS"})

# 🔹 OPEN_TICKET
open_templates = [
    "öppna {} {}",
    "visa {} {}",
    "{} {}",
    "visa {} nummer {}",
]
for i in range(1, 51):
    for t in open_templates:
        intents.append({
            "text": t.format("ärende", i),
            "intent": "OPEN_TICKET"
        })

# 🔹 KB_SEARCH
kb_phrases = [
    "vpn fungerar inte",
    "problem med vpn",
    "kan inte logga in vpn",
    "lösenord fungerar inte",
    "glömt lösenord",
    "outlook kraschar",
    "wifi långsamt",
    "server access",
    "behöver behörighet",
]
for p in kb_phrases:
    intents.append({"text": p, "intent": "KB_SEARCH"})

# 🔹 SMALLTALK
smalltalk = [
    "hej",
    "hallå",
    "tjena",
    "god morgon",
    "god kväll",
    "ville bara säga hej",
    "hej på dig",
]
for s in smalltalk:
    intents.append({"text": s, "intent": "SMALLTALK"})

# 🔹 HELP
help_phrases = [
    "hjälp",
    "vad kan du göra",
    "hur funkar detta",
    "visa kommandon",
    "hjälp mig",
]
for h in help_phrases:
    intents.append({"text": h, "intent": "HELP"})

# 🔹 UNKNOWN (noise)
noise = [
    "asdfgh",
    "qwerty",
    "jag vill flyga",
    "vad är meningen med livet",
    "pizza",
]
for n in noise:
    intents.append({"text": n, "intent": "UNKNOWN"})

with open(OUT / "intent_dataset.json", "w", encoding="utf-8") as f:
    json.dump(intents, f, ensure_ascii=False, indent=2)

print(f"✅ Synthetic intent-dataset skapat ({len(intents)} rader)")
