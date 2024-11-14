import asyncio
from bot.test_openArticleFromHome import get_article_data

res = asyncio.run(get_article_data("https://apnews.com/politics"))
print(res)