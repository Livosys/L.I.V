#!/bin/bash

OUT="/opt/shix/logs/python_deps_$(date +%F_%H%M).log"

source /opt/shix/venv/bin/activate
pip freeze > $OUT

echo "PIP FREEZE DONE → $OUT"
