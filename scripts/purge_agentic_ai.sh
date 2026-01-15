#!/bin/bash

systemctl stop agentic-ai.service 2>/dev/null
systemctl disable agentic-ai.service 2>/dev/null
systemctl mask agentic-ai.service 2>/dev/null

rm -f /etc/systemd/system/agentic-ai.service
rm -rf /opt/shix/agent
rm -rf /opt/shix/agentic*
