import asyncio
import time

#########################
#########################
# This is the core logic of how the bot works. I trimmed off some non-essential functions like sending the message to a user and formatting.

from bot.test_openArticleFromHome import get_article_data
from bot.get_summary import create_summary
from bot.parse_response import parse_response

async def makeReport():
        get_article_data_time, create_summary_time = -1, -1
        try:
            # Fetch article data
            url = "https://apnews.com/politics"

            start = time.perf_counter()
            article_data = await get_article_data(url)
            end = time.perf_counter()
            get_article_data_time = end-start

            if (article_data != 0):
                start = time.perf_counter()
                response = create_summary(article_data)
                end = time.perf_counter()
                create_summary_time = end-start

                summary, key_terms = parse_response(response)
            else:
                raise Exception("Timeout Error")
            
            if get_article_data_time == -1 or create_summary_time == -1:
                 raise Exception("Something went wrong")
            else:
                 return [get_article_data_time, create_summary_time]
        except Exception as e:
            print(f"Error occured: {e}")
            return -1

#########################
#########################

# Measure times runs makeReport 100 times and stores the time it takes to execute each core function
def measure_times() -> list:
    res = []
    for i in range(100):
        print(i)
        res.append(asyncio.run(makeReport()))
    
    return res

# Get success rate gets the overall success rate of beginning to end article retrieval and summary generation
def get_success_rate(items: list) -> float:
    count = 0
    total = len(items)

    for item in items:
         if item == -1:
              count += 1
    
    return ( (total - count) / total ) * 100

# Get averages gets the
def get_averages(items: list) -> list:
    total_successes = 0
    sum_l = 0
    sum_r = 0

    for item in items:
        if item != -1:
            total_successes += 1
            sum_l += item[0]
            sum_r += item[1]
    
    return sum_l / total_successes, sum_r / total_successes


    
times = measure_times()
print(get_success_rate(times))
print(get_averages(times))