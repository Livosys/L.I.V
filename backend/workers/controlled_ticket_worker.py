import requests

BACKEND_URL = "http://127.0.0.1:8000/freshservice/tickets/controlled"

def run():
    try:
        r = requests.get(BACKEND_URL, timeout=5)
        print("Worker run OK:", r.status_code, r.text)
    except Exception as e:
        print("Worker error:", str(e))

if __name__ == "__main__":
    run()
