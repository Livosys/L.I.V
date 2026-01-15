#!/bin/bash

OUT="/opt/shix/logs/mcp_patterns_$(date +%F_%H%M).log"

grep -R -n -E "tool|function_call|json schema|intent|planner|execute|dispatch" \
  /opt/shix/backend >> $OUT 2>/dev/null

echo "MCP PATTERN SCAN DONE → $OUT"
