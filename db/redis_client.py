import redis
import os
from dotenv import load_dotenv

load_dotenv()

def get_redis_connection():
    return redis.Redis(
        host = os.getenv("REDIS_HOST"),
        port = os.getenv("REDIS_PORT"),
        db = 0,
        password = os.getenv("REDIS_PASSWORD"),
        decode_responses=True)