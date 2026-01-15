import requests

def check():
    r = requests.get("http://127.0.0.1:8000/health", timeout=5)
    return r.status_code, r.text
