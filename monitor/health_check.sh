#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

URL="http://127.0.0.1:8000/health"
LOG="/opt/shix/data/health_monitor.log"

if ! /usr/bin/curl -sf "$URL" > /dev/null; then
  echo "$(date -u) HEALTH CHECK FAILED" >> "$LOG"
else
  echo "$(date -u) OK" >> "$LOG"
fi
