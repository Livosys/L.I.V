#!/bin/bash

SNAPSHOT_DIR="/opt/shix/rollback"

LAST=$(ls -1 "$SNAPSHOT_DIR" | sort | tail -n 1)

if [ -z "$LAST" ]; then
  echo "❌ Ingen rollback-punkt hittades"
  exit 1
fi

TARGET="$SNAPSHOT_DIR/$LAST"

echo "♻️  L.I.V – Återställer rollback-punkt:"
echo "   $TARGET"

# Restore backend
tar -xzf "$TARGET/shix_backend.tar.gz" -C /

# Restore systemd
tar -xzf "$TARGET/systemd_shix_backend.tar.gz" -C / 2>/dev/null

# Restore nginx
tar -xzf "$TARGET/nginx.tar.gz" -C /

systemctl daemon-reload
systemctl restart shix-backend
systemctl restart nginx

echo "✅ Återställning klar"
