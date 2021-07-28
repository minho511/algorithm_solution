import sys
import heapq
input = sys.stdin.readline
n = int(input())
q = []
std = int(input())
cnt = 0
for i in range(n-1):
    m = int(input())
    heapq.heappush(q, (-m, m))
while q:
    a, b = heapq.heappop(q)
    if b >= std:
        heapq.heappush(q, (-(b-1), b-1))
        std += 1
        cnt += 1
print(cnt)