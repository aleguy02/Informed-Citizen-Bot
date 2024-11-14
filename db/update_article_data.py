import time
import asyncio
from redis_client import get_redis_connection
from get_article_data_playwright import get_article_data # TODO: what the fuck is a relative import rahhhh. JS master race

url = "https://apnews.com/politics"
r = get_redis_connection()

while True:
    article_data = 0
    while article_data == 0:
        article_data = asyncio.run(get_article_data(url))

    print("setting data")
    r.hset("article_data", mapping=article_data)
    time.sleep(300)

