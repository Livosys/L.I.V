#!/bin/bash
set -e

BACKUP_FILE="$1"

if [ -z "$BACKUP_FILE" ]; then
  echo "Usage: restore_neo4j.sh <backup_file.tar.gz>"
  exit 1
fi

echo "Stopping Neo4j..."
docker stop neo4j

echo "Removing existing data..."
docker run --rm -v neo4j_data:/data alpine rm -rf /data/*

echo "Restoring backup..."
docker run --rm \
  -v neo4j_data:/data \
  -v "$(dirname $BACKUP_FILE)":/backup \
  alpine \
  tar xzf /backup/$(basename $BACKUP_FILE) -C /

echo "Starting Neo4j..."
docker start neo4j

echo "Neo4j restore completed."
