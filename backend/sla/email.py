import smtplib
from email.mime.text import MIMEText
from sla.config import SMTP_HOST, SMTP_USER, SMTP_PASS, ALERT_EMAIL

def send_email_alert(subject: str, body: str):
    if not all([SMTP_HOST, SMTP_USER, SMTP_PASS, ALERT_EMAIL]):
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = ALERT_EMAIL

    with smtplib.SMTP(SMTP_HOST, 587) as s:
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)
