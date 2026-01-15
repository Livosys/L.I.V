TRADEMARK = "SHIX™ — Designed & Trademarked by Liv. Dawod"

LICENSES = {
    "free": 1000,
    "pro": 10000,
    "enterprise": 100000
}

def check_usage(plan, used):
    return used <= LICENSES.get(plan, 0)
