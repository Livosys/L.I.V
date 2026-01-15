#!/bin/bash

echo "============================================"
echo " SHIX BACKEND DIAGNOSTICS"
echo "============================================"
echo ""

echo "---- 1) SYSTEMD ENVIRONMENT VARIABLES ----"
systemctl show shix-backend | grep Environment || echo "No environment variables found in systemctl."

echo ""
echo "---- 2) .env FILE PERMISSIONS ----"
ls -l /home/shix.livosys.se/backend/.env || echo ".env file not found!"

echo ""
echo "---- 3) .env CONTENT (SAFE MODE) ----"
if [ -f /home/shix.livosys.se/backend/.env ]; then
    sed -E 's/(=.*)/=********/g' /home/shix.livosys.se/backend/.env
else
    echo ".env missing!"
fi

echo ""
echo "---- 4) SYSTEMD SERVICE FILE ----"
cat /etc/systemd/system/shix-backend.service

echo ""
echo "---- 5) CHECK SYSTEMD ERRORS (LAST 40 LINES) ----"
journalctl -u shix-backend -n 40 --no-pager

echo ""
echo "---- 6) PYTHON VERSION ----"
python3 --version

echo ""
echo "---- 7) CHECK UVICORN PROCESS ----"
ps aux | grep uvicorn | grep -v grep || echo "No uvicorn process running."

echo ""
echo "---- 8) NETWORK LISTENING ON PORT 8000 ----"
ss -tulpn | grep 8000 || echo "Nothing running on port 8000."

echo ""
echo "---- 9) VERIFY FILE OWNERSHIP IN BACKEND ----"
ls -l /home/shix.livosys.se/backend

echo ""
echo "============================================"
echo " DIAGNOSTICS COMPLETE"
echo "============================================"
