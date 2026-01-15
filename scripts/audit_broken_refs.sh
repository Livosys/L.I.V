#!/bin/bash

OUT="/opt/shix/logs/broken_refs_$(date +%F_%H%M).log"
mkdir -p /opt/shix/logs

echo "=== SYSTEMD FILES ===" >> $OUT
grep -R "agent\\|grafana\\|prometheus\\|diagnostic_agent" /etc/systemd/system >> $OUT 2>/dev/null

echo -e "\n=== SHIX BACKEND ===" >> $OUT
grep -R "agent\\|grafana\\|prometheus\\|diagnostic_agent" /opt/shix/backend >> $OUT 2>/dev/null

echo -e "\n=== SHIX ROOT ===" >> $OUT
grep -R "agent\\|grafana\\|prometheus\\|diagnostic_agent" /opt/shix >> $OUT 2>/dev/null

echo -e "\n=== PYTHON ENV ===" >> $OUT
grep -R "agent\\|grafana\\|prometheus" /opt/shix/venv >> $OUT 2>/dev/null

echo "AUDIT DONE → $OUT"
