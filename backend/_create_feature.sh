#!/bin/bash
set -e

NAME="$1"

mkdir -p "/opt/shix/backend/${NAME}"

cat << 'EOT' > "/opt/shix/backend/${NAME}/__init__.py"
# feature package
EOT

cat << 'EOT' > "/opt/shix/backend/${NAME}/core.py"
def setup(app=None):
    return app
EOT

echo "Feature ${NAME} created"
