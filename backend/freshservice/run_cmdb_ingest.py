import os
import sys

BASE_DIR = "/opt/shix/backend"
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from freshservice.cmdb_ingest import ingest_ticket_to_cmdb

# TEST med verifierat ticket-id
TICKETS_TO_INGEST = [4]

def main():
    for tid in TICKETS_TO_INGEST:
        try:
            result = ingest_ticket_to_cmdb(tid)
            print("OK:", result)
        except Exception as e:
            print("ERROR:", tid, str(e))

if __name__ == "__main__":
    main()
