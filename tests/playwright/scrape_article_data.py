from db.utils import scrape_article_data

import asyncio
print(asyncio.run(scrape_article_data("https://apnews.com/politics")))