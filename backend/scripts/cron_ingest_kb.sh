#!/bin/bash

export PYTHONPATH=/opt/shix/backend
export TENANT_ID=customer1

/opt/shix/venv/bin/python /opt/shix/backend/rag/ingest_kb.py >> /opt/shix/data/cron_kb_ingest.log 2>&1
