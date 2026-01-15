#!/bin/bash
source /opt/shix/venv/bin/activate
export PYTHONPATH=/opt/shix/backend
python - << 'PY'
from ingest.ingest_tickets import ingest_tickets
ingest_tickets("customer1-prod-key", limit=50)
PY
