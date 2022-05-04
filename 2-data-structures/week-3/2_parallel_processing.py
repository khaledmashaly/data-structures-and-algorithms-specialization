# python3
import heapq as h

n, m = [int(i) for i in input().split(' ')]
t = [int(i) for i in input().split(' ')]

threads = []

for i in range(0, n):
    new_thread = (0, i)
    h.heappush(threads, new_thread)

for process in t:
    ready_thread = h.heappop(threads)
    start_time = ready_thread[0]
    thread_id = ready_thread[1]

    print(thread_id, start_time)

    finish_time = start_time + process
    running_thread = (finish_time, thread_id)
    h.heappush(threads, running_thread)
