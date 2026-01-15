from sla.slack import send_slack_alert
from sla.email import send_email_alert

def alert_if_breached(ticket):
    if ticket.get("sla_status") == "breached":
        msg = f"SLA BREACHED: #{ticket['id']} – {ticket['title']}"
        send_slack_alert(msg)
        send_email_alert("SLA Breach", msg)
