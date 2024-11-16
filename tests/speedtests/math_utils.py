# Get success rate gets the overall success rate of beginning to end article retrieval and summary generation
def get_success_rate(items: list) -> float:
    count = 0
    total = len(items)

    for item in items:
         if item == -1:
              count += 1
    
    return ( (total - count) / total ) * 100    #      succeeded tries         *    100
                                                # --------------------------
                                                        # total tries


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