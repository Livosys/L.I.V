#!/bin/bash

OUT="/opt/shix/logs/agentic_rag_audit_$(date +%F_%H%M).log"
mkdir -p /opt/shix/logs

echo "=== DIRECTORY TREE (SHIX) ===" >> $OUT
find /opt/shix -maxdepth 4 -type d >> $OUT

echo -e "\n=== FILES CONTAINING KEYWORDS ===" >> $OUT
grep -R -n -E "agent|agentic|mcp|tool|rag|vector|semantic|planner|orchestr|decision|policy" \
  /opt/shix >> $OUT 2>/dev/null

echo -e "\n=== PYTHON MODULES (BACKEND) ===" >> $OUT
find /opt/shix/backend -type f -name "*.py" >> $OUT

echo -e "\n=== RAG DATA ===" >> $OUT
ls -R /opt/shix/data >> $OUT 2>/dev/null

echo -e "\n=== SYSTEMD REFERENCES ===" >> $OUT
grep -R -E "agent|agentic|mcp" /etc/systemd/system >> $OUT 2>/dev/null

echo "AUDIT DONE → $OUT"
