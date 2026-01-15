import redis

_redis = None

def get_redis():
    global _redis
    if _redis is None:
        _redis = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )
    return _redis
