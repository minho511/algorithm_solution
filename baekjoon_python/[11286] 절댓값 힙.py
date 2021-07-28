# 2021 07 25 자료 구조 우선순위 큐
# https://www.acmicpc.net/problem/11286
import sys; input = sys.stdin.readline
import heapq
n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q,(abs(x),x))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)