#!/bin/bash

systemctl stop prometheus-node-exporter.service 2>/dev/null
systemctl disable prometheus-node-exporter.service 2>/dev/null
systemctl mask prometheus-node-exporter.service 2>/dev/null

for t in $(systemctl list-unit-files | grep prometheus-node-exporter | awk '{print $1}'); do
  systemctl stop $t 2>/dev/null
  systemctl disable $t 2>/dev/null
  systemctl mask $t 2>/dev/null
done

apt purge -y prometheus-node-exporter
apt autoremove -y

rm -rf /etc/prometheus
rm -rf /var/lib/prometheus
rm -rf /var/log/prometheus
