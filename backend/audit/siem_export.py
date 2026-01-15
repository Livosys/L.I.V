import json, requests, os

SIEM_URL = os.getenv("SIEM_WEBHOOK")

def export(event):
    if not SIEM_URL: return
    requests.post(SIEM_URL, json=event, timeout=5)
