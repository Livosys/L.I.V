#!/bin/bash
set -e

BACKUP_DIR="/opt/shix/backups"
DATE=$(date +"%Y%m%d_%H%M%S")

mkdir -p "$BACKUP_DIR"

echo "Stopping Neo4j..."
docker stop neo4j

echo "Backing up Neo4j volume..."
docker run --rm \
  -v neo4j_data:/data \
  -v "$BACKUP_DIR":/backup \
  alpine \
  tar czf /backup/neo4j_backup_$DATE.tar.gz /data

echo "Starting Neo4j..."
docker start neo4j

echo "Neo4j backup completed: neo4j_backup_$DATE.tar.gz"
