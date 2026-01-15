import time

def audit(event: str, intent: str):
    print(f"{time.time()} | {event} | {intent}")
