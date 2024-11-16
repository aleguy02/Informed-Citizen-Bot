import asyncio
import time


# /////////////////////////
# This is the core logic of how the bot works. I trimmed off some non-essential functions like sending the message to a user and formatting.

from bot_deprecated.test_openArticleFromHome import get_article_data
from bot_deprecated.get_summary import create_summary
from bot_deprecated.parse_response import parse_response

async def makeReport():
        TIME_playwright, TIME_groq = -1, -1
        try:
            # Fetch article data
            url = "https://apnews.com/politics"

            start = time.perf_counter()
            article_data = await get_article_data(url)
            end = time.perf_counter()
            TIME_playwright = end-start

            if (article_data != 0):
                start = time.perf_counter()
                response = create_summary(article_data)
                end = time.perf_counter()
                TIME_groq = end-start

                summary, key_terms = parse_response(response)
            else:
                raise Exception("Timeout Error")
            
            if TIME_playwright == -1 or TIME_groq == -1:
                 raise Exception("Something went wrong")
            else:
                 return [TIME_playwright, TIME_groq]
        except Exception as e:
            print(f"Error occured: {e}")
            return -1

# /////////////////////////



# Measure times runs makeReport 100 times and stores the time it takes to execute each core function
def measure_times() -> list:
    res = []
    for i in range(100):
        print(i)
        res.append(asyncio.run(makeReport()))
    
    return res

from math_utils import get_success_rate, get_averages

times = measure_times()

print(get_success_rate(times))

print(get_averages(times))