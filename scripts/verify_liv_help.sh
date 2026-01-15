#!/bin/bash

grep -R "hjälp" /opt/shix/backend >/dev/null && echo "✅ L.I.V hjälp finns kvar" || echo "❌ L.I.V hjälp saknas"
