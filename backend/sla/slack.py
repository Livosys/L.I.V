import requests
from sla.config import SLACK_WEBHOOK

def send_slack_alert(text: str):
    if not SLACK_WEBHOOK:
        return
    requests.post(SLACK_WEBHOOK, json={"text": text}, timeout=5)
