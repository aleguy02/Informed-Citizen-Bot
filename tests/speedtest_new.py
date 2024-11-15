import time

#########################
#########################
# This is the core logic of how the bot works. I trimmed off some non-essential functions like sending the message to a user and formatting.

from bot_deprecated.test_openArticleFromHome import get_article_data
from bot_deprecated.get_summary import create_summary
from bot_deprecated.parse_response import parse_response

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
    pass

from math_utils import get_success_rate, get_averages
times = measure_times()
print(get_success_rate(times))
print(get_averages(times))