#!/bin/bash

SERVICES=(
  grafana-server.service
  prometheus.service
  agentic-ai.service
)

for svc in "${SERVICES[@]}"; do
  systemctl stop "$svc" 2>/dev/null
  systemctl disable "$svc" 2>/dev/null
  systemctl mask "$svc" 2>/dev/null
done
