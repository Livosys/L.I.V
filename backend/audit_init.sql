CREATE TABLE IF NOT EXISTS audit_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  actor TEXT,
  action TEXT,
  ticket_id INTEGER,
  metadata TEXT,
  created_at TEXT
);

CREATE TABLE IF NOT EXISTS access_requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER,
  user TEXT,
  status TEXT,
  created_at TEXT
);
