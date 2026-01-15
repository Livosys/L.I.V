from collections import Counter

def detect_pattern(tickets: list):
    subjects = [t["subject"] for t in tickets if "subject" in t]
    common = Counter(subjects).most_common(1)

    if common and common[0][1] >= 3:
        return {
            "type": "problem",
            "signature": common[0][0]
        }
    return None
