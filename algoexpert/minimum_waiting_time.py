# O(NlogN) time | O(1) space
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    prev_query_wait_time = 0
    total_wait_time = 0
    for i in range(1, len(queries)):
        wait_time = prev_query_wait_time + queries[i - 1]
        total_wait_time += wait_time
        prev_query_wait_time = wait_time
    return total_wait_time
