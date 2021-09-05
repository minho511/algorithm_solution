import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    l = len(food_times)
    _sum = 0
    previous = 0
    while _sum + ((q[0][0] - previous) * l) <= k:
        now = heapq.heappop(q)[0]
        _sum += (now-previous) * l
        l-=1
        previous = now
    res = sorted(q, key=lambda x: x[1])
    return res[(k-_sum)%l][1]