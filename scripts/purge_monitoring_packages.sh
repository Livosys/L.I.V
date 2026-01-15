#!/bin/bash

apt purge -y grafana grafana-server prometheus prometheus-node-exporter 2>/dev/null
apt autoremove -y
