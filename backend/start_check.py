import sys

print("Python:", sys.version)

def check(name, fn):
    try:
        fn()
        print(f"{name} OK")
    except Exception as e:
        print(f"{name} FAIL:", e)

check("auth.guard", lambda: __import__("auth.guard"))
check("observability.middleware", lambda: __import__("observability.middleware"))
check("observability.tracing", lambda: __import__("observability.tracing"))
check("routers.chat", lambda: __import__("routers.chat"))

print("START CHECK DONE")
