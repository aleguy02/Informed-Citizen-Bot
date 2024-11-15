import redis
import os
from dotenv import load_dotenv

load_dotenv()

def get_article_data():
    r = redis.Redis(
        host = os.getenv("REDIS_HOST"),
        port = os.getenv("REDIS_PORT"),
        db = 0,
        password = os.getenv("REDIS_PASSWORD"),
        decode_responses=True
        )
    
    article_data = r.hgetall("article_data")

    if not article_data:
        print("No values at key")
        return 0 # returns 0 if there is no article data
    return {
                "headline": article_data["headline"],
                "article": article_data["article"],
                "url": article_data["url"]
            }