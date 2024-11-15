import asyncio
import time

import bot.utils as utils

async def makeReport():
    get_article_data_time, create_summary_time = -1, -1
    try:
        article_data = utils.get_article_data()
        # if getting the article data raises a timeout error then don't even try to make a summary, just send a message saying there was an
        if article_data == 0:
            raise RuntimeError("Getting article data failed")

        # Generate summary and list
        summary = utils.create_summary(article_data["article"])
        key_terms_str = utils.get_key_terms(article_data["article"])
        key_terms = utils.format_terms(key_terms_str)
        if key_terms == 0:
            raise RuntimeError("Key terms formatting error")
        
        # Send summary and URL to the Discord channel
    except Exception as e:
        print(f"Error occured: {e}")