#!/bin/bash
set -e

echo "Running start_check..."
PYTHONPATH=/opt/shix/backend /opt/shix/venv/bin/python start_check.py

echo "Running main_check..."
PYTHONPATH=/opt/shix/backend /opt/shix/venv/bin/python main_check.py

echo "ALL CHECKS PASSED"

echo "Checking /api/chat route..."
curl -sf http://127.0.0.1:8000/api/chat -X POST \
  -H "Content-Type: application/json" \
  -d '{"ping":"pong"}' > /dev/null

echo "/api/chat OK"
