import requests
from pathlib import Path

SIEM_ENDPOINT = "https://siem.example.com/ingest"
AUDIT_LOG = Path("/opt/shix/data/audit.log")

def export():
    if not AUDIT_LOG.exists():
        return

    with AUDIT_LOG.open() as f:
        for line in f:
            requests.post(
                SIEM_ENDPOINT,
                data=line,
                headers={"Content-Type": "application/json"},
                timeout=2
            )

if __name__ == "__main__":
    export()
