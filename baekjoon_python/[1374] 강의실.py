# 2021 07 29
# https://www.acmicpc.net/problem/1374
import sys; input = sys.stdin.readline
import heapq
n = int(input())
q = []
p = []
for _ in range(n):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (b,c))
start , end = heapq.heappop(q)
heapq.heappush(p, end)
while q:
    start, end = heapq.heappop(q)
    if p[0] <= start:
        heapq.heappop(p)
    heapq.heappush(p, end)
print(len(p))