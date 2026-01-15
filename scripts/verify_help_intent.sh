#!/bin/bash

grep -R '"intent": "HELP"' /opt/shix/backend >/dev/null \
  && echo "✅ HELP-intent finns kvar" \
  || echo "❌ HELP-intent SAKNAS"
