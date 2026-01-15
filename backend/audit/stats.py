import json
from collections import Counter

LOG_FILE = "/opt/shix/data/audit.log"

def intent_stats():
    counts = Counter()
    with open(LOG_FILE) as f:
        for line in f:
            entry = json.loads(line)
            counts[entry["intent"]] += 1
    return dict(counts)
