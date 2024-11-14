from .redis_client import get_redis_connection

def get_article_data():
    r = get_redis_connection()
    article_data = r.hgetall("article_data")

    if not article_data:
        print("No values at key")
        return 0 # returns 0 if there is no article data
    return {
                "headline": article_data["headline"],
                "article": article_data["article"],
                "url": article_data["url"]
            }