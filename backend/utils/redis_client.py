import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")

r = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True
)
