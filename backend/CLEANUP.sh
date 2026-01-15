#!/bin/bash
set -e

echo "== STOP SERVICE =="
systemctl stop shix-backend || true

echo "== REMOVE OLD TEMP FILES =="
rm -f /opt/shix/backend/*.bak || true
rm -f /opt/shix/backend/*.old || true
rm -f /opt/shix/backend/*.tmp || true

echo "== REMOVE PYTHON CACHE =="
find /opt/shix/backend -type d -name "__pycache__" -exec rm -rf {} + || true
find /opt/shix/backend -type f -name "*.pyc" -delete || true

echo "== REMOVE UNUSED / LEGACY FILES =="
rm -f /opt/shix/backend/_reset_systemd.sh || true

echo "== VERIFY CORE FILES EXIST =="
test -f /opt/shix/backend/main.py
test -f /opt/shix/backend/start_check.py
test -f /opt/shix/backend/main_check.py
test -f /opt/shix/backend/DEPLOY_GUARD.sh
test -f /opt/shix/backend/_create_feature.sh
test -f /opt/shix/backend/feature_loader.py

echo "== PERMISSIONS =="
chmod +x /opt/shix/backend/DEPLOY_GUARD.sh
chmod +x /opt/shix/backend/_create_feature.sh

echo "== START SERVICE =="
systemctl daemon-reload
systemctl start shix-backend

echo "== DONE CLEANUP =="
