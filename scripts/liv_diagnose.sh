#!/bin/bash

echo "🧪 L.I.V – DIAGNOSE (READ-ONLY)"
echo "======================================================"
echo "🕒 Tid: $(date)"
echo "🖥 Host: $(hostname)"
echo "👤 User: $(whoami)"
echo "======================================================"

echo "🔎 BACKEND STATUS"
systemctl is-active shix-backend || true
ss -lntp | grep -E ':(8000|9000)\s' || true
echo "------------------------------------------------------"

echo "🧩 LOVABLE UI-KONTRAKT (DETEKTION)"
echo "• List-läge (items): STÖDS"
echo "• Actions / externa länkar: BLOCKERADE I LOVABLE"
echo "• Cards / blocks: EJ STÖDDA (kan orsaka UI-fel)"
echo "⚠️ VARNING:"
echo "  Externa länkar (href/url/markdown) renderas INTE klickbara i nuvarande Lovable."
echo "  Rekommendation: visa instruktion eller ID, ej länkar."
echo "------------------------------------------------------"

echo "🧪 PAYLOAD-KONTROLL (SENASTE TEST)"
curl -s -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"öppna 4"}' | jq '.'
echo "------------------------------------------------------"

echo "✅ DIAGNOSE KLAR"
