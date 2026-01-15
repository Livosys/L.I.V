import os

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")
ALERT_EMAIL = os.getenv("ALERT_EMAIL_TO")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
