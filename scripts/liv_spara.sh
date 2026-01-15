#!/bin/bash

SNAPSHOT_DIR="/opt/shix/rollback"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
TARGET="$SNAPSHOT_DIR/$TIMESTAMP"

mkdir -p "$TARGET"

echo "💾 L.I.V – Skapar rollback-punkt: $TIMESTAMP"

# SHIX backend
tar -czf "$TARGET/shix_backend.tar.gz" /opt/shix/backend

# systemd service
tar -czf "$TARGET/systemd_shix_backend.tar.gz" /etc/systemd/system/shix-backend.service /etc/systemd/system/shix-backend.service.d 2>/dev/null

# nginx config
tar -czf "$TARGET/nginx.tar.gz" /etc/nginx

# metadata
cat << META > "$TARGET/info.txt"
Rollback created: $TIMESTAMP
Host: $(hostname)
User: $(whoami)
Reason: liv spara
META

echo "✅ Rollback-punkt sparad i:"
echo "   $TARGET"
