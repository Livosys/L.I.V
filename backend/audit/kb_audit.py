import json, time

def log(event):
    event["ts"] = int(time.time())
    with open("/opt/shix/logs/kb_audit.log","a") as f:
        f.write(json.dumps(event)+"\n")
