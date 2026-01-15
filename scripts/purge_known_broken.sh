#!/bin/bash

# systemd services
for svc in $(systemctl list-unit-files | egrep "agentic|grafana|prometheus" | awk '{print $1}'); do
  systemctl stop $svc 2>/dev/null
  systemctl disable $svc 2>/dev/null
  systemctl mask $svc 2>/dev/null
  rm -f /etc/systemd/system/$svc
done

# systemd overrides
rm -rf /etc/systemd/system/*.service.d

# files & dirs
rm -rf /opt/shix/agent
rm -rf /opt/shix/agentic*
rm -rf /opt/shix/backend/*agent*
rm -rf /etc/grafana /var/lib/grafana /var/log/grafana
rm -rf /etc/prometheus /var/lib/prometheus /var/log/prometheus

# python cache
find /opt/shix -type d -name "__pycache__" -exec rm -rf {} +
find /opt/shix -type f -name "*.pyc" -delete

echo "PURGE COMPLETE"
