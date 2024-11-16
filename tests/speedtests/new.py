import asyncio
import time

import bot.utils as utils

def makeReport():
    TIME_redis, TIME_groq = -1, -1
    try:
        # Time redis
        start = time.perf_counter()
        article_data = utils.get_article_data()
        end = time.perf_counter()
        TIME_redis = end-start
        
        if article_data == 0:
            raise RuntimeError("Getting article data failed")

        #Time groq
        start = time.perf_counter()
        summary = utils.create_summary(article_data["article"])
        key_terms_str = utils.get_key_terms(article_data["article"])
        end = time.perf_counter()
        TIME_groq = end-start

        key_terms = utils.format_terms(key_terms_str)
        if key_terms == 0:
            raise RuntimeError("Key terms formatting error")
        
        if TIME_redis == -1 or TIME_groq == -1:
            raise Exception("Something went wrong")
        else:
            return [TIME_redis, TIME_groq]
        # Send summary and URL to the Discord channel
    except Exception as e:
        print(f"Error occured: {e}")
        return -1



# Measure times runs makeReport 100 times and stores the time it takes to execute each core function
from tests.speedtests.math_utils import get_success_rate, get_averages

def measure_times() -> list:
    res = []
    for i in range(100):
        print(i)
        res.append(makeReport())
    
    return res


times = measure_times()

print(get_success_rate(times))

print(get_averages(times))