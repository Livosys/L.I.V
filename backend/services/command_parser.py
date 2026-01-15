import re

def parse_command(message: str):
    text = message.lower().strip()

    match_change = re.search(r"simulera\s+change\s+([a-z0-9\-]+)", text)
    if match_change:
        return ("SIMULATE_CHANGE", match_change.group(1).upper())

    return (None, None)
